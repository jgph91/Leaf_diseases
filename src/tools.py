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

def labels(label_list):
    '''Transform Image Labels uisng Scikit Learn's LabelBinarizer'''

    label_binarizer = LabelBinarizer()
    image_labels = label_binarizer.fit_transform(label_list)
    pickle.dump(label_binarizer,open('/output/label_transform.pkl', 'wb'))
    n_classes = len(label_binarizer.classes_)

    return label_binarizer.classes_