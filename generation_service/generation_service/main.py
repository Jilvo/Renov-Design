from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "")
    print(data)
    if not prompt or prompt == "":
        return {"code": 400, "message": "Prompt is empty!"}
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

        image.save(f"{id_of_prompt}.png")
        print("Image generated successfully!")
        return {
            "code": 200,
            "id": id_of_prompt,
            "message": "Image generated successfully!",
        }
    except Exception as e:
        return {"code": 500, "message": "Error in generating image!", "error": str(e)}


if __name__ == "__main__":
    app.run(debug=True)
