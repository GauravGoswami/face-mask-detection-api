from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os

class MaskDetectorModel():
    
    model = None
    net = None

    def predict(self, image):

        # load the input image from disk, clone it, and grab the image spatial
        # dimensions
        
        orig = image.copy()
        (h, w) = image.shape[:2]

        blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
            (104.0, 177.0, 123.0))

        # perform face detection
        self.net.setInput(blob)
        detections = self.net.forward()
        
        results_list = []

        # loop over the detections and store predictions for each
        for i in range(0, detections.shape[2]):
            
            confidence = detections[0, 0, i, 2]

            # filter out weak detections
            if confidence > 0.5:
                
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                (startX, startY) = (max(0, startX), max(0, startY))
                (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

                # preprocessing for the mask detection model based on how it was trained
                
                face = image[startY:endY, startX:endX]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)
                face = np.expand_dims(face, axis=0)
                
                mask, withoutMask = self.model.predict(face)[0]
                results_list.append([int(startX), int(endX), int(startY), int(endY), float(mask)])
                
        return results_list            
                
    def __init__(self, model_dir='./Models'):
        
        # Load and init models
        
        prototxtPath = os.path.sep.join([model_dir, "deploy.prototxt"])
        weightsPath = os.path.sep.join([model_dir,
            "res10_300x300_ssd_iter_140000.caffemodel"])
        self.net = cv2.dnn.readNet(prototxtPath, weightsPath)

        self.model = load_model(os.path.sep.join([model_dir, 'mask_detector.model']))