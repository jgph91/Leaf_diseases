from src.web_scrap import get_ai
from src. predict import predict,crop_disease_transformation
from src.pesticidesDB import get_pesticides
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pygubu
import os
import tkinter as tk


class Application:
    def __init__(self, master):


        self.root = tk.Tk()
        self.root.withdraw()

        #1: Create a builder
        self.builder = builder = pygubu.Builder()
        #2: Load an ui file
        builder.add_from_file('interface.ui')
        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('main', master)
        builder.connect_callbacks(self)
        self.filepath = builder.get_object('filepath')
        self.result = builder.get_object("resultdisease")
       
        self.pesticides = builder.get_object('resultpesticide')
    
        
    def image_selector(self, event=None):
        '''Select image of the leaf'''
        
        self.imagepath = self.filepath.cget('path')
        messagebox.showinfo('Image selected', self.imagepath)
        self.root.update_idletasks()

    def click_disease(self):
        '''Applies the predictor to the specified image'''
        
        res = predict(self.imagepath)
        self.result.configure(text=res)
        self.root.update_idletasks()
    
    def disease_input(self):
        '''Select the disease'''

        self.entry = self.builder.get_object('Select_disease')
        self.disease = self.entry.get()
        self.root.update_idletasks()
        

    def click_ai(self):
        '''Returns an excel file with the available Ai's'''

        self.disease_input()
        crop,disease = crop_disease_transformation(self.disease)
        get_ai(crop,disease)
        self.root.update_idletasks()


    def insert_ai(self):
        '''Select the Ai'''

        self.entry2 = self.builder.get_object('query_pesticides')
        self.ai = self.entry2.get()
        self.root.update_idletasks()
    

    def click_pesticides(self):
        '''Returns the list of available pesticides for the specified Ai'''
        
        self.insert_ai()
        pesticides = get_pesticides(self.ai)
        self.pesticides.configure(text=pesticides)
        self.root.update_idletasks()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

