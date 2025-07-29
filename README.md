✅ README.md – Project Overview

# 🖼️ Text-to-Image GenAI

This project uses Stable Diffusion to generate images from natural language prompts using Python and Flask.

---

## 🚀 Features

- Generate images from any English text prompt
- API powered by Flask
- Uses Hugging Face `diffusers` with Stable Diffusion
- Returns file path for generated images
- Includes endpoint to serve images via HTTP

---

## 📦 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/payal211/text2image-genai.git
   cd text2image-genai


Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
```
bash
pip install -r requirements.txt
```
🧠 Usage
Start the Flask API
```
bash
python FLASK_API.py
```


🔽 Step 1: Download the Model Locally
You can use Hugging Face's CLI to download:
```
bash
huggingface-cli login  # optional, if model is gated

# Download all files to a folder
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
```

or just download using python file
```
pip install -U huggingface-hub

RUN: python download_model.py
```

Example API Request
```
bash
curl -X POST http://localhost:5000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt": "A cat playing piano in space"}'
```
Get Generated Image
Visit:
```
bash
http://localhost:5000/image/generated_YYYYMMDD_HHMMSS.png
```

📁 Project Structure
```
bash

├── text2image-genai/
   ├── app.py               # Flask API
   ├── generator.py         # Image generation logic
   ├── utils.py             # Helper functions
   ├── requirements.txt     # Dependencies
   ├── outputs/             # Generated images
   └── README.md            # Documentation
   ├── ./stable-diffusion-v1-5/
   ├── model_index.json
      ├── scheduler/
      ├── unet/
      ├── vae/
      ├── tokenizer/
      ├── text_encoder/
```
🧩 Optional Enhancements
Add Streamlit or Gradio UI

Upload prompts from text files

Deploy to Hugging Face Spaces, Render, or Docker

🧠 Model Info
Uses runwayml/stable-diffusion-v1-5 via Hugging Face Diffusers.


## ✅ Optional: Streamlit UI (`streamlit_app.py`)

Run the streamlit app:
```
bash
streamlit run streamlit_app.py
```
