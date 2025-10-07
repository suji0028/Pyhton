import os
from huggingface_hub import InferenceClient
from PIL import Image
import io

client = InferenceClient(
    model="black-forest-labs/FLUX.1-Kontext-dev",
    token=os.environ["HF_TOKEN"]
)

with open("cat.png", "rb") as image_file:
    input_image = Image.open(io.BytesIO(image_file.read()))

# output is a PIL.Image object
image = client.image_to_image(
    image=input_image,
    prompt="Turn the cat into a tiger.",
)
