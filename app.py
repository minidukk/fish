from flask import Flask, request, render_template, jsonify
from keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)

# Tải mô hình nhận diện cá cảnh
model = load_model('./fish_classification_model.keras')

# Các lớp cá cảnh
classes = ['betta fish', 'corydoras fish', 'discus fish', 'flowerhorn fish', 
                'goldfish fish', 'guppy fish', 'koi fish', 'neon fish', 
                'oscar fish', 'platy fish']

# Trang chủ với giao diện tải ảnh lên
@app.route('/')
def index():
    return render_template('index.html')

# API xử lý nhận diện hình ảnh
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file found"}), 400

    file = request.files['file']
    image = Image.open(file).resize((224, 224))
    image = np.expand_dims(image, axis=0) 

    predictions = model.predict(image)
    predicted_class = classes[np.argmax(predictions)]

    return jsonify({"prediction": predicted_class})
