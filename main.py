from src.tools import convert_image_to_array,labels
import numpy as np
import pickle
import cv2
from os import listdir
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import LabelBinarizer
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation, Flatten, Dropout, Dense
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing import image

def main():

    directory_root = '../color'

    image_list, label_list = [], []
    image_size = 0
    try:
        print("[INFO] Loading images ...")
        root_dir = listdir(directory_root)

        for plant_folder in root_dir :#get the plant folders name in the root directory
            plant_disease_folder_list = listdir(f"{directory_root}/{plant_folder}")

            for plant_disease_folder in plant_disease_folder_list:#get the disease folder name
                print(f"[INFO] Processing {plant_disease_folder} ...")
                plant_disease_image_list = listdir(f"{directory_root}/{plant_folder}/{plant_disease_folder}/")

                #transformation of images into np arrays
                for image in plant_disease_image_list[:150]:#specify the number of images loaded per folder
                    image_directory = f"{directory_root}/{plant_folder}/{plant_disease_folder}/{image}"
                    if (image_directory.endswith(".jpg") == True) or (image_directory.endswith(".JPG") == True):
                        image_list.append(convert_image_to_array(image_directory))
                        label_list.append(plant_disease_folder)

        print("[INFO] Image loading completed")  

    except Exception as e:
        print(f"Error : {e}")

    image_size = len(image_list)
    print(f'{len(image_list)} images have been processed!')

    #Getting labels for every class
    label_binarizer = LabelBinarizer()
    image_labels = label_binarizer.fit_transform(label_list)
    #save labels using pickle
    pickle.dump(label_binarizer,open('./output/label_transform.pkl', 'wb'))
    n_classes = len(label_binarizer.classes_)
    print(label_binarizer.classes_)

    np_image_list = np.array(image_list, dtype=np.float16) / 255.0 #preprocessing the images

    print("[INFO] Spliting data to train, test")
    x_train, x_test, y_train, y_test = train_test_split(np_image_list, 
                                                        image_labels, test_size=0.2, random_state = 42) 

    #image params
    
    width=256
    height=256
    depth=3

    #performs random picture rotations to increase accuracy of the model using less samples
    aug = ImageDataGenerator(
    rotation_range=25, width_shift_range=0.1,
    height_shift_range=0.1, shear_range=0.2, 
    zoom_range=0.2,horizontal_flip=True, 
    fill_mode="nearest")

    #CNN model

    model = Sequential()
    inputShape = (height, width, depth)
    chanDim = -1

    if K.image_data_format() == "channels_first":
        chanDim = 1
    model.add(Conv2D(32, (3, 3), padding="same",input_shape=inputShape))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(128, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(128, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(1024))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(n_classes))
    model.add(Activation("softmax"))
    
    model.summary()

    #CNN params

    EPOCHS = 25
    INIT_LR = 1e-3
    BS = 32

    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
    # distribution

    
    model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["categorical_accuracy"])
    # train the network
    print("[INFO] training network...")

    #
    history = model.fit_generator(
    aug.flow(x_train, y_train, batch_size=BS),
    validation_data=(x_test, y_test),
    steps_per_epoch=len(x_train) // BS,
    epochs=EPOCHS, verbose=1
    )

    #Accuracy of the model
    print("[INFO] Calculating model accuracy")
    scores = model.evaluate(x_test, y_test)
    print(f"Test Accuracy: {scores[1]*100}")

    # save the model to disk
    print("[INFO] Saving model...")
    pickle.dump(model,open('output/cnn_model.pkl', 'wb'))
 

if __name__ == '__main__':
    main()