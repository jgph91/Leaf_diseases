from os import listdir
import cv2
import numpy as np
import pickle
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import LabelBinarizer

def convert_image_to_array(image_dir):
    '''Transform a picture into an array'''

    default_image_size = tuple((256, 256))
    try:
        image = cv2.imread(image_dir)
        if image is not None :
            image = cv2.resize(image, default_image_size)   
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None

def image_collector(directory_root,images_processed):
    '''Return two list: pictures converted and '''

    image_list, label_list = [], []
    image_size = 0

    try:
        print("[INFO] Loading images ...")
        root_dir = listdir(directory_root)

        for plant_folder in root_dir:  # get the plant folders name in the root directory
            plant_disease_folder_list = listdir(
                f"{directory_root}/{plant_folder}")

            for plant_disease_folder in plant_disease_folder_list:  # get the disease folder name
                print(f"[INFO] Processing {plant_disease_folder} ...")
                plant_disease_image_list = listdir(
                    f"{directory_root}/{plant_folder}/{plant_disease_folder}/")

                # transformation of images into np arrays
                # specify the number of images loaded per folder
                for image in plant_disease_image_list[:images_processed]:
                    image_directory = f"{directory_root}/{plant_folder}/{plant_disease_folder}/{image}"
                    if (image_directory.endswith(".jpg") == True) or (image_directory.endswith(".JPG") == True):
                        image_list.append(convert_image_to_array(image_directory))
                        label_list.append(plant_disease_folder)

        print("[INFO] Image loading completed")

    except Exception as e:
        print(f"Error : {e}")

    image_size = len(image_list)
    print(f'{len(image_list)} images have been processed!')

    return image_list,label_list