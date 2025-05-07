import os
import re
import base64
from PIL import Image
from openai import OpenAI

# Instantiate OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o"  # Vision-capable model


def extract_calories(text: str) -> str:
    """
    Extract the first calorie figure (e.g., '450 kcal') from text.
    """
    m = re.search(r"(\d{2,5})\s*(?:k?cal(?:ories)?|cal)", text, re.IGNORECASE)
    if m:
        return f"{m.group(1)} kcal"
    return text.strip()


def estimate_calories(pil_img: Image.Image) -> str:
    """
    Save PIL image, encode to Base64, send to OpenAI Vision model,
    and return the parsed calorie estimate.
    """
    tmp = "temp.png"
    pil_img.save(tmp)
    with open(tmp, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    os.remove(tmp)

    data_uri = f"data:image/png;base64,{b64}"
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": (
                "You are a nutrition assistant. Estimate the TOTAL calories in the image (just a number + kcal)."
            )},
            {"role": "user", "content": [
                {"type": "text", "text": "Estimate calories:"},
                {"type": "image_url", "image_url": {"url": data_uri}}
            ]}
        ],
        temperature=0.2,
        max_tokens=100,
    )
    return extract_calories(resp.choices[0].message.content)