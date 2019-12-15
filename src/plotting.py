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

def confusion_matrix(y_test,y_pred,labels):
    
    #Confussion matrix
    ax = plt.subplot()
    matrix = confusion_matrix(y_test, y_pred, labels=labels)
    matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]
    # Plot the matrix
    sns.heatmap(matrix,annot=True)
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels'); 
    ax.set_title('Confusion Matrix'); 
    ax.xaxis.set_ticklabels(labels)
    ax.yaxis.set_ticklabels(labels)  

    return '[INFO] Plotting finished!'
