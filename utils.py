# utils.py

import os
from datetime import datetime

def create_output_dir(directory: str):
    """
    Creates the output directory if it doesn't exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_timestamped_filename(prefix="image", extension="png"):
    """
    Returns a timestamped filename like image_20250728_141200.png
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"
