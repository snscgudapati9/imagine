from flask import Flask, request, send_file
import torch
from PIL import Image
from io import BytesIO

app = Flask(_name_)

# Load your AI model (AnimeGAN or CartoonGAN)
# Assuming we have a pre-trained model loaded here

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    img = Image.open(file)

    # Apply the model to convert to anime/cartoon (pseudo code)
    # processed_image = apply_model(img)
    
    # Convert processed image back to bytes and send back to frontend
    output = BytesIO()
    img.save(output, format='PNG')
    output.seek(0)

    return send_file(output, mimetype='image/png')

if _name_ == '_main_':
    app.run(debug=True)