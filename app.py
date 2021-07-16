from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
from flask_cors import CORS
from MaskDetectorModel import MaskDetectorModel
import cv2
import os

app = Flask(__name__)
cors = CORS(app)

global mask_detector_model

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        file = request.files['image']
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        prediction = mask_detector_model.predict(image)
        return(jsonify({
            "Status":"Success",
            "Results":prediction}))
    except Exception as e:
        return jsonify({
            "Status":"Failure",
            "Error":str(e)})

if __name__ == '__main__':
    PORT = 8190
    #force CPU only mode
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    #initialize model instance
    mask_detector_model = MaskDetectorModel()
    app.run(debug=True, host='0.0.0.0', port=PORT)