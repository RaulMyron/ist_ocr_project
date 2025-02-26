import ollama
import base64


def ocr_image(image_path):
    with open(image_path, "rb") as img:
        img_base64 = base64.b64encode(img.read()).decode("utf-8")

    response = ollama.chat(
        "llama3.2-vision",
        [
            {
                "role": "user",
                "content": f"whats in this image {img_base64} give just the text",
            }
        ],
    )
    return response["message"]["content"]


print(ocr_image("assets/semana_07ex/pagina_1.png"))
