# app.py

from flask import Flask, request, jsonify, send_file
from generator import generate_image
from utils import create_output_dir
import os

app = Flask(__name__)
OUTPUT_DIR = "outputs"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Text-to-Image GenAI API!",
        "usage": "POST /generate with JSON body {'prompt': 'your text here'}"
    })

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        image_path = generate_image(prompt, output_dir=OUTPUT_DIR)
        return jsonify({
            "message": "Image generated successfully",
            "image_path": image_path
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/image/<filename>", methods=["GET"])
def serve_image(filename):
    """
    Serve image files from the outputs directory.
    """
    filepath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(filepath):
        return send_file(filepath, mimetype="image/png")
    return jsonify({"error": "Image not found"}), 404

if __name__ == "__main__":
    create_output_dir(OUTPUT_DIR)
    app.run(debug=True)
