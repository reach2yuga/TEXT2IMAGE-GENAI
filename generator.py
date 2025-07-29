# generator.py

from diffusers import StableDiffusionPipeline
import torch
from utils import create_output_dir, get_timestamped_filename

# Load the model once at module level
def load_model(model_id="runwayml/stable-diffusion-v1-5"):
    """
    Loads the Stable Diffusion model.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    pipeline = pipeline.to(device)
    return pipeline

pipe = load_model()

# Load model locally once at module level
def load_model_locally(model_path="./stable-diffusion-v1-5"):
    """
    Loads Stable Diffusion from a local directory.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"

    pipe = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    pipe.to(device)
    return pipe

# pipe_locally = load_model_locally()

def generate_image(prompt: str, output_dir: str = "outputs") -> str:
    """
    Generate an image from a text prompt and save it to output_dir.
    Returns the path to the saved image.
    """
    create_output_dir(output_dir)
    # image = pipe_locally(prompt).images[0]
    # if model is from huggingface
    image = pipe(prompt).images[0]
    filename = get_timestamped_filename(prefix="generated", extension="png")
    filepath = f"{output_dir}/{filename}"
    image.save(filepath)
    return filepath
