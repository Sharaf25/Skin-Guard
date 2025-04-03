from flask import Flask, request, send_from_directory, jsonify
from PIL import Image
import numpy as np
import skin_cancer_detection as SCD
import os

app = Flask(__name__, static_folder=".", static_url_path="")  # Serve static files from the project directory

# Route for the home page
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Route for the about page
@app.route("/about")
def about():
    return send_from_directory(".", "about.html")

# Route for the check your skin page
@app.route("/check")
def check():
    return send_from_directory(".", "check.html")

# Route to handle image upload and analysis
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        # Process the uploaded image
        inputimg = Image.open(file)
        inputimg = inputimg.resize((28, 28))
        img = np.array(inputimg).reshape(-1, 28, 28, 3)

        # Predict the result using the model
        prediction = SCD.model.predict(img)
        prediction = prediction.tolist()
        max_prob = max(prediction[0])
        class_ind = prediction[0].index(max_prob)
        result = SCD.classes[class_ind]

        # Additional information based on the prediction
        info = SCD.get_info(class_ind)

        return jsonify({"result": result, "info": info}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)