# streamlit_app.py

import streamlit as st
from generator import generate_image
from PIL import Image

st.title("🖼️ Text to Image Generator")
st.write("Enter a text prompt and generate an image using Stable Diffusion.")

prompt = st.text_input("Enter prompt", value="A futuristic city skyline at night")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image_path = generate_image(prompt)
        st.image(Image.open(image_path), caption="Generated Image")
        st.success(f"Saved to: {image_path}")