import matplotli.pyplot as plot
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd()))

def plotting_train(history):
    ''' Plots showing losses and accuracy of the model'''

    #Plotting params
    acc = history.history['accuracy']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)
    # Train and validation accuracy
    plt.plot(epochs, acc, 'b', label='Training accurarcy')
    plt.plot(epochs, val_acc, 'r', label='Validation accurarcy')
    plt.title('Training and Validation accurarcy')
    plt.legend()
    plt.figure()
    # Train and validation loss
    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title('Training and Validation loss')
    plt.legend()
    plt.show()

def confusion_matrix(model_dir,weights_dir):
    '''Creates the confusion matrix'''

    #perform a new test
    x_train, x_test, y_train, y_test = train_test_split(np_image_list,image_labels, test_size=0.2, random_state=42)
    # load json and create model
    json_file = open(model_dir, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(weights_dir)
    print("Loaded model from disk")

    Y_pred = loaded_model.predict(x_test)
    Y_true = y_test
    Y_pred = loaded_model.predict(x_test)
    # Convert predictions classes to one hot vectors 
    Y_pred_classes = np.argmax(Y_pred,axis = 1) 
    # Convert validation observations to one hot vectors
    print(Y_pred_classes)
    Y_true = np.argmax(y_test,axis = 1)
    print(Y_true)
    # compute the confusion matrix
    cm = confusion_matrix(Y_true, Y_pred_classes)
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    # plot the confusion matrix
    f,ax = plt.subplots(figsize=(8, 8))
    sns.heatmap(cm, annot=True, linewidths=0.01,cmap="Greens",linecolor="gray", fmt= '.1f',ax=ax)
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")
    plt.show()

    return '[INFO] Plotting finished!'
