import os
from flask import Flask, jsonify, request
from timeit import default_timer as timer

app = Flask(__name__)


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


@app.route("/modify", methods=["GET"])
def modify_image():
    start = timer()
    from diffusers import AutoPipelineForImage2Image
    from diffusers.utils import load_image
    import torch
    import os

    # Utiliser un chemin absolu pour charger l'image
    image_path = os.path.abspath("kitchen.png")
    import uuid

    id_of_prompt = str(uuid.uuid4().hex)
    if not os.path.exists(image_path):
        return jsonify({"code": 404, "message": "Image not found"}), 404

    pipe = AutoPipelineForImage2Image.from_pretrained(
        "stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16"
    )
    pipe.to("cuda")

    init_image = load_image(image_path).resize((512, 512))

    prompt = "Modify this image of a kitchen to change the style to a more rustic one with wood"

    image = pipe(
        prompt,
        image=init_image,
        num_inference_steps=2,
        strength=0.5,
        guidance_scale=0.0,
    ).images[0]
    image.save(f"{id_of_prompt}.png")
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
