import ollama
import base64


def ocr_image(image_path):
    with open(image_path, "rb") as img:
        img_base64 = base64.b64encode(img.read()).decode("utf-8")

    response = ollama.chat(
        "minicpm-v",
        [
            {
                "role": "user",
                "content": f"Extract and transcribe all text from this image: data:image/png;base64,{img_base64}",
            }
        ],
    )

    with open("output.txt", "w") as f:
        f.write(response["message"]["content"])


ocr_image("assets/semana_07ex/pagina_1.png")
