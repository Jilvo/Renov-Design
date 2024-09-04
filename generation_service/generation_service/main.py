import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from timeit import default_timer as timer
import uuid

app = Flask(__name__)
CORS(app)


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

    # user_id = data.get("user_id", "")
    # Utiliser un chemin absolu pour charger l'image
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
    if style_name not in styles_dict:
        return jsonify({"code": 400, "message": "Invalid style"}), 400
    # filename = secure_filename(file.filename)
    id_of_prompt = str(uuid.uuid4().hex)
    if not os.path.exists(user_id):
        os.makedirs(user_id)
    save_path = f"{user_id}/{id_of_prompt}_init.png"
    file.save(save_path)
    prompt = styles_dict[style_name]
    # You can now use the saved image and style name to process further
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
    image.save(f"{user_id}/{id_of_prompt}.png")
    print("Image generated successfully!")
    end = timer()
    return jsonify(
        {
            "code": 200,
            "generation_duration": round(end - start, 1),
            "path": f"{id_of_prompt}.png",
            "message": "Image generated successfully!",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
