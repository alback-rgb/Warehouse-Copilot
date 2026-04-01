from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

from prompts import LAYOUT_ANALYSIS_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_layout(image_bytes):

    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": LAYOUT_ANALYSIS_PROMPT},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
        max_output_tokens=800,
    )

    return response.output_text