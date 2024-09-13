import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from timeit import default_timer as timer
import uuid
import boto3
from botocore.client import Config
import requests
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generate", methods=["POST"])
def generate_image():
    start = timer()
    data = request.get_json()
    prompt = data.get("prompt", "")
    user_id = data.get("user_id", "")
    print(data)
    if not prompt or prompt == "":
        return {"code": 400, "message": "Prompt is empty!"}
    if not user_id or user_id == "":
        return {"code": 400, "message": "User ID is empty!"}
    try:
        from diffusers import AutoPipelineForText2Image
        import torch
        import uuid

        id_of_prompt = str(uuid.uuid4().hex)
        print(f"ID of prompt: {id_of_prompt}")
        pipe = AutoPipelineForText2Image.from_pretrained(
            "stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16"
        )
        pipe.to("cuda")

        image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
        if not os.path.exists(user_id):
            os.makedirs(user_id)
        image.save(f"{user_id}/{id_of_prompt}.png")
        print("Image generated successfully!")
        end = timer()
        return {
            "code": 200,
            "id": id_of_prompt,
            "path": f"{user_id}/{id_of_prompt}.png",
            "generation_duration": round(end - start, 1),
            "message": "Image generated successfully!",
        }
    except Exception as e:
        return {"code": 500, "message": "Error in generating image!", "error": str(e)}


@app.route("/modify", methods=["POST"])
def modify_image():
    if "file" not in request.files:
        return jsonify({"code": 400, "message": "No file part"}), 400
    file = request.files["file"]
    style_name = request.form.get("styleName", "")
    user_id = request.form.get("userId", "")

    if file.filename == "":
        return jsonify({"code": 400, "message": "No selected file"}), 400
    if not style_name:
        return jsonify({"code": 400, "message": "Style name is required"}), 400
    if not user_id:
        return jsonify({"code": 400, "message": "userId is required"}), 400
    print("Modifying image...")
    start = timer()
    from diffusers import AutoPipelineForImage2Image
    from diffusers.utils import load_image
    import torch
    import os

    styles_dict = {
        "0": "Transform the image to reflect a clean, streamlined design with handle-less cabinets, smooth surfaces, and a neutral color palette featuring whites, grays, and black accents.",  # noqa: E501
        "1": "Modify the image to include rustic elements like raw wood cabinetry, open shelving, and accessories in wrought iron or copper.",  # noqa: E501
        "2": "Adapt the image with features typical of Scandinavian design, such as light wood tones, simple lines, and functionality, accented with pastel colors.",  # noqa: E501
        "3": "Rework the image to showcase industrial elements like exposed piping, metal light fixtures, and a use of materials like stainless steel and concrete for a robust feel.",  # noqa: E501
        "4": "Alter the image to embody a traditional aesthetic with ornate woodwork, classic details, and rich color schemes, often incorporating patterns like plaids or florals.",  # noqa: E501
        "5": "Update the image to exhibit Art Deco flair with geometric patterns, bold streamlined forms, and luxurious materials like marble and gold.",  # noqa: E501
        "6": "Revise the image to blend contemporary design with eclectic accessories, featuring a mix of modern lines and varied textures or global décor influences.",  # noqa: E501
        "7": "Enhance the image to depict a high-tech kitchen with the latest appliances, smart home technology, and a sleek, modern look that incorporates glossy surfaces and high-end materials.",  # noqa: E501
        "8": "Transform the kitchen image to a bohemian style with vibrant colors, mixed patterns, and a collection of eclectic, artisanal, and vintage decor.",  # noqa: E501
        "9": "Modify the image to present a farmhouse style with apron sinks, open shelving, and a mix of rustic and modern elements that create a cozy, welcoming space.",  # noqa: E501
    }  # noqa: E501

    bucket_name = os.getenv("S3_BUCKET_NAME")
    access_key = os.getenv("S3_ACCESS_KEY")
    secret_key = os.getenv("S3_SECRET_KEY")

    if style_name not in styles_dict:
        return jsonify({"code": 400, "message": "Invalid style"}), 400

    id_of_prompt = str(uuid.uuid4().hex)

    if not os.path.exists(user_id):
        os.makedirs(user_id)
    save_path = f"{user_id}/{id_of_prompt}_init.png"
    file.save(save_path)
    prompt = styles_dict[style_name]
    print("Style: ", style_name)
    print("Prompt: ", prompt)

    if not os.path.exists(save_path):
        return jsonify({"code": 404, "message": "Image not found"}), 404

    pipe = AutoPipelineForImage2Image.from_pretrained(
        "stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16"
    )
    pipe.to("cuda")

    init_image = load_image(save_path).resize((512, 512))

    prompt = "Modify this image of a kitchen to change the style to a more rustic one with wood"

    image = pipe(
        prompt,
        image=init_image,
        num_inference_steps=2,
        strength=0.5,
        guidance_scale=0.0,
    ).images[0]
    output_path = f"{user_id}/{id_of_prompt}.png"
    image.save(output_path)
    print("Image generated successfully!")
    end = timer()

    # Upload Original to S3
    upload_to_scaleway(
        bucket_name, save_path, f"renov-design/{save_path}", access_key, secret_key
    )

    # Upload Modified to S3
    upload_to_scaleway(
        bucket_name, output_path, f"renov-design/{output_path}", access_key, secret_key
    )

    # Supprimer les fichiers locaux après l'upload
    try:
        os.remove(save_path)
        os.remove(output_path)
        print(f"Local files {save_path} and {output_path} deleted.")
    except Exception as e:
        print(f"Error deleting local files: {e}")
    store_datas(
        f"renov-design/{save_path}",
        f"renov-design/{output_path}",
        user_id,
        tag=style_name,
        processing_duration=round(end - start, 1),
    )
    return jsonify(
        {
            "code": 200,
            "processing_duration": round(end - start, 1),
            "modified_image": f"renov-design/{save_path}",
            "origin_path": f"renov-design/{output_path}",
            "tags": style_name,
            "message": "Image generated successfully!",
        }
    )


def store_datas(modified_image, origin_path, user_id, tag, processing_duration):
    data = {
        "created_by": user_id,
        "tags": tag,
        "status": "PENDING",
        "modified_image": modified_image,
        "generation_origin": origin_path,
        "processing_duration": processing_duration,
    }
    print("Storing data...", data)
    response = requests.post(
        "http://127.0.0.1:8000/stockage/prompts",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),  # Convertir les données en JSON
    )
    print("Response from server:", response.status_code, response.text)


def upload_to_scaleway(
    bucket_name, file_path, object_name, access_key, secret_key, region="fr-par"
):
    # Créer un client S3 compatible Scaleway
    s3 = boto3.client(
        "s3",
        region_name=region,
        endpoint_url=f"https://s3.{region}.scw.cloud",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
    )

    try:
        # Uploader le fichier
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {object_name} in bucket {bucket_name}.")
    except Exception as e:
        print(f"Error uploading file: {e}")


if __name__ == "__main__":
    app.run(debug=True)
