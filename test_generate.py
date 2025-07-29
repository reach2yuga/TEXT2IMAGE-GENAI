from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load model
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)
pipe.to(device)

# Generate image
prompt = "A cozy cabin in the snowy woods at night"
image = pipe(prompt).images[0]

# Save and show image
image.save("generated_image.png")
image.show()
