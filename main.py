from src.webscrap import get_ai
from src. predict import predict,crop_disease_transformation
from src.pesticidesDB import get_pesticides
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pygubu
import os
import tkinter as tk



class Application:
    def __init__(self, master):


        self.root = tk.Tk()
        self.root.withdraw()


        #1: Create a builder
        self.builder = builder = pygubu.Builder()
        self.result = self.builder.get_object('Text_1')
        self.ai
        self.pesticides

        #2: Load an ui file
        builder.add_from_file('interface.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow', master)

    def click_button_1(self,img_dir):
        res = predict(img_dir)
        self.result.configure(text=res)
        self.root.update_idletasks()
        

    def click_button_2(self,result):

        crop,disease = crop_disease_transformation(result)
        ai = get_ai(crop,disease)

        return ai
    
    def click_button_3(self,ai):

        pesticides = get_pesticides(ai)

        return pesticides

    CLASSES = ['Grape___Black_rot', 'Grape___Esca_(Black_Measles)',
     'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
     'Pepper_bell___Bacterial_spot', 'Pepper_bell___healthy',
     'Tomato___Bacterial_spot', 'Tomato___Early_blight' ,'Tomato___Late_blight',
     'Tomato___Septoria_leaf_spot', 'Tomato___Target_Spot',
     'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']







if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

