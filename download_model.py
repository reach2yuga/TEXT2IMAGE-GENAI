from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="runwayml/stable-diffusion-v1-5",
    local_dir="./stable-diffusion-local",
    local_dir_use_symlinks=False  # important for Windows
)