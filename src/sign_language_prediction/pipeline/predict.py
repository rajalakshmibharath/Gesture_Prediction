import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename): 
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))
		
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))

        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)

        predictions = model.predict(test_image)
        class_index = np.argmax(predictions, axis=1)
        class_probabilities = predictions[0, class_index]
        print(class_index)

       
        class_labels = {
            0: 'Class _',
            1: 'Class 0',
            2: 'Class 1',
            3: 'Class 2',
            4: 'Class 3',
            5: 'Class 4',
            6: 'Class 5',
            7: 'Class 6',
            8: 'Class 7',
            9: 'Class 8',
            10: 'Class 9',
            11: 'Class A',
            12: 'Class B',
            13: 'Class C',
            14: 'Class D',
            15: 'Class E',
            16: 'Class F',
            17: 'Class G',
            18: 'Class H',
            19: 'Class I',
            20: 'Class J',
            21: 'Class K',
            22: 'Class L',
            23: 'Class M',
            24: 'Class N',
            25: 'Class O',
            26: 'Class P',
            27: 'Class Q',
            28: 'Class R',
            29: 'Class S',
            30: 'Class T',
            31: 'Class U',
            32: 'Class V',
            33: 'Class W',
            34: 'Class X',
            35: 'Class Y',
            36: 'Class Z',
            
        }
        
        prediction = class_labels.get(class_index[0], 'Unknown')
        
        return [{"image": prediction, "probability": float(class_probabilities)}]