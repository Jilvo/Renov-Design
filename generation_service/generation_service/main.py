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
import uvicorn
from asgiref.wsgi import WsgiToAsgi
from PIL import Image
app = Flask(__name__)
CORS(app)
load_dotenv()


@app.route("/")
def hello_world():
    print("Hello!")
    return "Hello!"

@app.route("/generate", methods=["POST"])
def generate_image():
    start = timer()
    data = request.get_json()
    prompt = data.get("prompt", "")
    user_id = data.get("user_id", "")
    print(prompt)
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
            "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16"
        )
        pipe.to("cuda")
        negative_prompt = (
            "low quality, blurry, distorted, extra fingers, deformed hands, bad anatomy, overexposed, underexposed,jpeg artifacts, worst quality, bad proportions, cropped, noise, glitch, mutated, bad perspective,anime style, cartoon, low resolution, oversaturated"
        )
        image = pipe(prompt=prompt, num_inference_steps=4, guidance_scale=5.0).images[0]
        image = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,  # Ajout du filtre anti-artefacts
            num_inference_steps=70,  # Augmenté pour plus de détails
            guidance_scale=7.5,  # Meilleur contrôle du rendu
            width=1024,  # Augmenter la largeur pour plus de détails
            height=1024,  # Ratio large pour capturer plus de la scène
        ).images[0]

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


@app.route("/generate_test", methods=["POST"])
def generate_test():
    start = timer()
    data = request.get_json()
    list_of_prompts = [
        "A serene sunset over a calm lake with trees and mountains in the background. A small boat floats on the water.",
        "A futuristic city at night with neon lights, flying cars, and tall skyscrapers.",
        "A silver-haired elf warrior holding a glowing sword in a magical forest with ancient trees.",
        "A fluffy orange cat curled up on a green velvet sofa in a cozy living room. Sunlight streams through the window, highlighting its fur. Behind the sofa, there’s a bookshelf with books and plants.",  # noqa: E501
    ]
    num_inference_steps = int(data.get("num_inference_steps", 1))
    guidance_scale = float(data.get("guidance_scale", 0.0))
    model = data.get("model", "sdxl-turbo")

    if num_inference_steps is None or num_inference_steps == "":
        return {"code": 400, "message": "Number of inference steps is empty!"}
    print("num_inference_steps: ", num_inference_steps)
    if guidance_scale is None or guidance_scale == "":
        return {"code": 400, "message": "Guidance scale is empty!"}
    if model is None or model == "":
        return {"code": 400, "message": "Model is empty!"}
    print("guidance_scale: ", guidance_scale)
    print("Lunch Model")
    try:
        import torch
        import uuid
        import os
        from diffusers import AutoPipelineForText2Image
        from diffusers import StableDiffusion3Pipeline

        if model == "sdxl-turbo":
            pipe = AutoPipelineForText2Image.from_pretrained(
                "stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16"
            )
        elif model == "sdxl":
            pipe = AutoPipelineForText2Image.from_pretrained(
                "stabilityai/sdxl", torch_dtype=torch.float16, variant="fp16"
            )
        elif model == "stable-diffusion-3-medium":
            pipe = StableDiffusion3Pipeline.from_pretrained(
                "stabilityai/stable-diffusion-3-medium-diffusers",
                torch_dtype=torch.float16,
            )
        else:
            return {"code": 400, "message": "Invalid model!"}
        id_of_prompt = str(uuid.uuid4().hex)
        print(f"ID of prompt: {id_of_prompt}")
        pipe.to("cuda")
        print("Generate image...")
        dict_of_duration = {}
        folder_name = str(round(guidance_scale, 1))  # Convertir en chaîne de caractères
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        for index, prompt in enumerate(list_of_prompts):
            print("Prompt: ", index, prompt)
            image = pipe(
                prompt=prompt,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                height=1024,
                width=1024,
            ).images[0]
            print(f"{folder_name}/{index}/{id_of_prompt}.png")
            if not os.path.exists(f"{model}/{folder_name}/{index}"):
                os.makedirs(f"{model}/{folder_name}/{index}")
            image.save(f"{model}/{folder_name}/{index}/{id_of_prompt}.png")
            print("Image generated successfully!")
            end = timer()
            print(
                f"End of loop for guidance_scale: {guidance_scale} with duration: {round(end - start, 1)}"
            )
            dict_of_duration[guidance_scale] = round(end - start, 1)
        print("End of loop for all prompts", dict_of_duration)
        return {
            "code": 200,
            "id": id_of_prompt,
            "path": f"{folder_name}/{index}/{id_of_prompt}.png",
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

    negative_prompts = {
        "0": "cluttered, excessive decorations, ornate, messy, bright neon colors, warm tones, textured surfaces, heavy wood grains, rustic, vintage, floral patterns, busy wallpaper, overly detailed, distressed materials, eclectic, old-fashioned, traditional, excessive contrast, harsh shadows",
        "1":"glossy surfaces, ultra-modern, sleek, industrial, glass-heavy, plastic materials, polished metal, futuristic, monochrome, geometric, minimalist, cold lighting, synthetic, excessive symmetry, ultra-clean lines",
        "2":"dark colors, heavy furniture, intricate designs, overdecorated, busy patterns, gothic, baroque, metal-heavy, industrial, excessive contrast, neon colors, overly ornate, heavy wood textures, dark lighting",
        "3":"soft pastel colors, floral patterns, polished marble, minimalistic clean lines, overly bright lighting, vintage, farmhouse, rustic wood-heavy, warm tones, bohemian, excessive softness, gold accents, plush furniture",
        "4":"ultra-modern, minimalist, industrial, glass-heavy, futuristic, high-tech, neon colors, monochrome, synthetic materials, clean lines, lack of decoration, open shelves, raw concrete, cold lighting, excessive white space",
        "5":"rustic, distressed wood, industrial, minimalist, farmhouse, Scandinavian, neutral tones, raw concrete, worn-out, country-style, random eclectic decor, overly simple, lack of symmetry",
        "6":"uniform, overly symmetrical, ultra-minimalist, excessive uniformity, dull colors, purely monochrome, industrial, completely rustic, heavy ornamentation, old-fashioned, traditional, cluttered, outdated",
        "7":"old-fashioned, vintage, rustic, ornate details, wood-heavy, cluttered, warm colors, floral patterns, farmhouse style, traditional, soft lighting, imperfect textures, natural imperfections",
        "8":"minimalist, monochrome, clinical, ultra-modern, metallic, high-tech, industrial, sharp edges, smooth surfaces, perfect symmetry, neutral colors, simple, polished",
        "9":"sleek, ultra-modern, industrial, polished metal, futuristic, monochrome, sharp angles, cold lighting, synthetic, neon accents, high-tech, minimalism, ultra-clean lines",
    }
    bucket_name = os.getenv("S3_BUCKET_NAME")
    access_key = os.getenv("S3_ACCESS_KEY")
    secret_key = os.getenv("S3_SECRET_KEY")

    if style_name not in styles_dict:
        return jsonify({"code": 400, "message": "Invalid style"}), 400

    id_of_prompt = str(uuid.uuid4().hex)

    if not os.path.exists(user_id):
        os.makedirs(user_id)
    origin_image_path = f"{user_id}/{id_of_prompt}_init.png"
    file.save(origin_image_path)
    with Image.open(origin_image_path) as img:
        width, height = img.size
    prompt = styles_dict[style_name]
    negative_prompt = negative_prompts[style_name]
    print("Style: ", style_name)
    print("Prompt: ", prompt)

    if not os.path.exists(origin_image_path):
        return jsonify({"code": 404, "message": "Image not found"}), 404
    width = round(width/3)
    height = round(height/3)
    print(f"Image dimensions: {width}x{height}")
    pipe = AutoPipelineForImage2Image.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16"
    )
    pipe.to("cuda")

    init_image = load_image(origin_image_path).resize((width, height))

    # prompt = "Modify this image of a kitchen to change the style to a more rustic one with wood"
    # Génération de l'image avec des paramètres ajustés
    image = pipe(
            prompt=prompt,
            image=init_image,
            negative_prompt=negative_prompt,  # Ajout du filtre anti-artefacts
            num_inference_steps=70,  # Augmenté pour plus de détails
            guidance_scale=7.0,  # Meilleur contrôle du rendu
            strength=0.4,  # Augmenter la force pour plus de changements
            width=width,  # Augmenter la largeur pour plus de détails
            height=height,  # Ratio large pour capturer plus de la scène
        ).images[0]
    modified_image_path = f"{user_id}/{id_of_prompt}.png"
    image.save(modified_image_path)
    print("Image generated successfully!")
    end = timer()

    # Upload Original to S3
    upload_to_scaleway(
        bucket_name,
        origin_image_path,
        f"renov-design/{origin_image_path}",
        access_key,
        secret_key,
    )

    # Upload Modified to S3
    upload_to_scaleway(
        bucket_name,
        modified_image_path,
        f"renov-design/{modified_image_path}",
        access_key,
        secret_key,
    )

    # Supprimer les fichiers locaux après l'upload
    try:
        os.remove(origin_image_path)
        os.remove(modified_image_path)
        print(f"Local files {origin_image_path} and {modified_image_path} deleted.")
    except Exception as e:
        print(f"Error deleting local files: {e}")
    store_datas(
        f"renov-design/{origin_image_path}",
        f"renov-design/{modified_image_path}",
        user_id,
        tag=style_name,
        processing_duration=round(end - start, 1),
    )
    return jsonify(
        {
            "code": 200,
            "processing_duration": round(end - start, 1),
            "origin_path": f"renov-design/{origin_image_path}",
            "modified_image": f"renov-design/{modified_image_path}",
            "tags": style_name,
            "message": "Image generated successfully!",
        }
    )


def store_datas(origin_path, modified_image, user_id, tag, processing_duration):
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
        "http://localhost:8081/stockage/prompts",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),  # Convertir les données en JSON
    )
    print("Response from server:", response.status_code, response.text)


def upload_to_scaleway(
    bucket_name, file_path, object_name, access_key, secret_key, region="fr-par"
):
    # Créer un client S3 compatible Scaleway
    print("bucket_name",bucket_name)
    print("file_path",file_path)
    print("object_name",object_name)
    print("access_key",access_key)
    print("secret_key",secret_key)

    s3 = boto3.client(
        "s3",
        region_name=region,
        endpoint_url=f"https://renov-design.s3.{region}.scw.cloud",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
    )

    try:
        # Uploader le fichier avec visibilité publique
        s3.upload_file(
            file_path, bucket_name, object_name, ExtraArgs={"ACL": "public-read"}
        )
        print(
            f"File {file_path} uploaded to {object_name} in bucket {bucket_name} with public access."
        )
    except Exception as e:
        print(f"Error uploading file: {e}")


asgi_app = WsgiToAsgi(app)
if __name__ == "__main__":
    uvicorn.run(asgi_app, host="localhost", port=9000)
    # uvicorn.run("generation_service.main:app", host="localhost", port=9000, debug=True)
