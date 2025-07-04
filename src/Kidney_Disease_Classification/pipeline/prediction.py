import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = tf.keras.models.load_model("artifacts/training/model.h5")

        # Preprocess image
        img = image.load_img(self.filename, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        # Predict
        prediction = model.predict(img_array)  # shape: (1, 1)
        prob = prediction[0][0]  # extract probability value

        if prob > 0.5:
            label = 'Tumor'
        else:
            label = 'Normal'

        return [{"image": label}]



