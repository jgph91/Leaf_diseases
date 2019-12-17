from src.image_collector import convert_image_to_array
import numpy as np
import os
import json
from keras.models import load_model
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

def predict(image_dir,model_dir,weight_dir):
    '''Predict the disease of the given photo'''
    
    CLASSES = ['Grape___Black_rot', 'Grape___Esca_(Black_Measles)',
     'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
     'Pepper_bell___Bacterial_spot', 'Pepper_bell___healthy',
     'Tomato___Bacterial_spot', 'Tomato___Early_blight' ,'Tomato___Late_blight',
     'Tomato___Septoria_leaf_spot', 'Tomato___Target_Spot',
     'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
    
    # load json and create model
    json_file = open(model_dir, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(weight_dir)
    print("Loaded model from disk")
    #image processing and recognition
    
    image_dir = convert_image_to_array(image_dir)
    np_image_li = np.array(image_dir, dtype=np.float16) / 255.0
    npp_image = np.expand_dims(np_image_li, axis=0)
    result=loaded_model.predict(npp_image)
    itemindex = np.where(result==np.max(result))
    print("probability:"+str(np.max(result))+"\n"+CLASSES[itemindex[1][0]])
    crop_disease = CLASSES[itemindex[1][0]]
    return crop_disease

def crop_disease_transformation(crop_disease):
    '''Returns crop and disease'''

    transformation = {'Grape___Black_rot': {'crop':'grape','disease':'black_rot'}, 
               'Grape___Esca_(Black_Measles)':{'crop':'grape','disease':'black_measles'},
               'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)':{'crop':None,'disease':None},
               'Grape___healthy':{'crop':None,'disease':None},
               'Pepper_bell___Bacterial_spot':{'crop':'pepper_bell','disease':'bacteria_spot_pepper'},
               'Pepper_bell___healthy':{'crop':None,'disease':None},
               'Tomato___Bacterial_spot':{'crop':'tomato','disease':'bacterial_spot'},
               'Tomato___Early_blight':{'crop':'tomato','disease':'alternaria_early_blight'} ,
               'Tomato___Late_blight':{'crop':'tomato','disease':'phytopthora_late_blight'},
               'Tomato___Septoria_leaf_spot':{'crop':'tomato','disase':'septoria_leaf_spot'},
               'Tomato___Target_Spot':{'crop':'tomato','disease':'bacterial_spot'},
               'Tomato___Tomato_mosaic_virus':{'mosaic_virus'},
               'Tomato___healthy':{'crop':None,'disease':None}}

    crop = transformation[crop_disease]['crop']
    disease = transformation[crop_disease]['disease']

    return crop,disease