from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY_2")
client = OpenAI(api_key=OPENAI_API_KEY)



response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role":"user", 
            "content": [
                {"type":"text", "text": "I want to list this item on my store. Write a listing title, description, condition, and name the manufacture.  If you can't tell give your best guess. Your output should be JSON. Write a JSON object with correct formatting, with the fields title, description, condition, manufacturer."},
                {
                    "type":"image_url", 
                    "image_url": {
                        "url": "https://www.soundguys.com/wp-content/uploads/2020/12/Apple-AirPods-Max-23-scaled.jpg"
                    },
                },
            ],
        },
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)

# Prompt without asking for JSON output
# Title: 
# "Modern Over-Ear Wireless Noise Cancelling Headphones with Smart Case - Sleek White"
# 
# Description:
# "Experience immersive sound quality with these state-of-the-art over-ear wireless headphones. Designed for comfort and convenience, they feature active noise c
# ancellation to block out unwanted background noise, allowing you to enjoy your music or calls without interruption. The sleek white design is not only stylish 
# but also durable. These headphones come with a smart matching case, ensuring that your audio gear stays protected while on the go. They offer easy connectivity
#  to your devices via Bluetooth technology and provide long hours of playback on a single charge."
# 
# Condition
# "Pre-owned - Excellent condition, fully functional with minimal signs of wear. Includes smart case."
# 
# Manufacturer:
# "Brand not specified - Best guess based on design and quality."
 

# Same prompt, but specifying output in JSON
# {
#   "title": "Wireless Over-Ear Headphones with Smart Case",
#   "description": "Experience high-quality sound and seamless connectivity with these sleek wireless over-ear headphones. Features comfortable cushioning for extended listening sessions and  active noise cancellation for an immersive audio experience. Comes with a stylish, protective smart case to keep your headphones safe on the go.",
#   "condition": "Used - Like New",
#   "manufacturer": "Manufacturer Unknown"
# }
 
def ebay_api_request(item):
    avg_price = avg(prices_first_page)
    return avg_price