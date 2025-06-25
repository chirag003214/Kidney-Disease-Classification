from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
import base64

from Kidney_Disease_Classification.utils.common import decodeImage
from Kidney_Disease_Classification.pipeline.prediction import PredictionPipeline    

# Set environment variables for locale
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# ✅ Move this to global scope
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

# Route: Home
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

# Route: Trigger Training (Optional)
@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")  # You can also run `dvc repro` here
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image_data = request.json['image']
        decodeImage(image_data, clApp.filename)  # Save the image
        result = clApp.classifier.predict()       # Run model prediction
        print("[PREDICTION RESULT]:", result)
        return jsonify(result)

    except Exception as e:
        print("[ERROR in /predict route]:", str(e))  # 👈 Add this line
        return jsonify({"error": str(e)}), 500


# Start the Flask app
if __name__ == "__main__":
    

    app.run(host='0.0.0.0', port=8080, debug=True)  # Set debug=True for development
