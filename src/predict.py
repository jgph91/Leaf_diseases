from src.image_collector import convert_image_to_array
import numpy as np
import os
import json
from keras.models import load_model
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

def predict(image_dir):
    '''Predict the disease of the given photo'''
    
    CLASSES = ['Grape_Black_rot', 'Grape_Black_Measles',
     'Grape_Leaf_blight', 'Grape_healthy',
     'Pepper_bell_Bacterial_spot', 'Pepper_bell_healthy',
     'Tomato_Bacterial_spot', 'Tomato_Early_blight' ,'Tomato_Late_blight',
     'Tomato_Septoria_leaf_spot', 'Tomato_Target_Spot',
     'Tomato_mosaic_virus', 'Tomato_healthy']
    
    # load json and create model
    json_file = open('./output/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights('./output/weights-improvement-70-0.97.hdf5')
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

    transformation = {'Grape_Black_rot': {'crop':'grape','disease':'black_rot'}, 
               'Grape_Black_Measles':{'crop':'grape','disease':'black_measles'},
               'Grape_Leaf_blight':{'crop':None,'disease':None},
               'Grape_healthy':{'crop':None,'disease':None},
               'Pepper_bell_Bacterial_spot':{'crop':'pepper_bell','disease':'bacteria_spot_pepper'},
               'Pepper_bell_healthy':{'crop':None,'disease':None},
               'Tomato_Bacterial_spot':{'crop':'tomato','disease':'bacterial_spot'},
               'Tomato_Early_blight':{'crop':'tomato','disease':'alternaria_early_blight'} ,
               'Tomato_Late_blight':{'crop':'tomato','disease':'phytopthora_late_blight'},
               'Tomato_Septoria_leaf_spot':{'crop':'tomato','disase':'septoria_leaf_spot'},
               'Tomato_Target_Spot':{'crop':'tomato','disease':'bacterial_spot'},
               'Tomato_mosaic_virus':{'crop':'tomato','disease':'mosaic_virus'},
               'Tomato_healthy':{'crop':None,'disease':None}}

    crop = transformation[crop_disease]['crop']
    disease = transformation[crop_disease]['disease']

    return crop,disease