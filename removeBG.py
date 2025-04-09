import os
import requests
import io
from PIL import Image

# Use environment variable for PhotoRoom API key
photoroom_key = os.getenv("PHOTOROOM_API_KEY")

def remove_bg(image_path):
    url = "https://sdk.photoroom.com/v1/segment"

    with open(image_path, "rb") as img_file:
        files = {
            "image_file": img_file
        }
        headers = {
            "Accept": "image/png",
            "x-api-key": photoroom_key
        }

        response = requests.post(url, files=files, headers=headers)

    if response.status_code == 200:
        png_image = Image.open(io.BytesIO(response.content)).convert("RGBA")
        white_bg = Image.new("RGB", png_image.size, (255, 255, 255))
        white_bg.paste(png_image, mask=png_image.split()[3])

        output_buffer = io.BytesIO()
        white_bg.save(output_buffer, format="JPEG")
        output_buffer.seek(0)
        return output_buffer
    else:
        raise Exception(f"PhotoRoom API error: {response.status_code} - {response.text}")
