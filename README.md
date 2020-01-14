# Plant diseases identifier

This app allows you to recognise the following plant diseases using a picture of one of its leaves:  

- Grape: black rot, black measles (scab) and leaf blight (leaf spot).  
- Pepper bell: bacterial spot.  
- Tomato: bacterial spot, early blight (Alternaria), late blight (Phytopthora), leaf spot (Septoria) and mosaic virus.  

In addition, it provides you with the info the available pesticides in Spain the fight the specified disease.  

<a href="https://github.com/jgph91"><img src="./input/CNN.png" title="Classes" alt="CNN"></a>
<!-- [![CNN]("./input/CNN.png")](https://github.com/jgph91) -->

## How to use this app

. Insert the leaf picture in the app.  
. Specify the crop and the disease to get the available Ai's in Spain. Please, ensure to have the proper geckodriver installed.    
. Select the Ai and get the available pesticides. Please, before running the query ensure to have permission to access to the database.      

## Used technologies in this project

- For the diseases identification it was used a convolutional neural network, which has a 97% of precission. Due to the size of the files the trained model it's not included in this repository, so you nedd to specify the directory where the model is located. However the training program its included in `CNN.py` and in colab `CNN.ipynb` if your computer it's not enough porwerful. Also it's included the `test.ipynb` in case you just want to test the CNN model, also you can find some pictures in `input/Test` if you want to run some tests.   
- To get the list of the allowed Ai's it was used selenium + mozilla firefox for web scraping the spanish Ministry of Agriculture webpage.
- The pesticides database it's stored in Atlas MongoDB cloud.
- The GUI was designed using TKinter and <a href="https://github.com/alejandroautalan/pygubu">Pygubu</a>.  

<a href="https://github.com/jgph91"><img src="./input/project.png" title="Project" alt="project"></a>
<!-- [![Project]("./input/project.png")](https://github.com/jgph91) -->

## Files included

- `CNN.py` -> CNN training + training plots display and confusion matrix.  
- `main.py` -> predictions function using the trained model.  
- `requeriments.txt` -> md file containing all the modules used in this app.
- `colab` -> CNN training + confusion matrix creation.  
- `src` -> auxiliary py's containing the functions used in the app and in the CNN train.

## Contact info

If you have any doubt please don't heisitate to contact me:

- email : jgph91@gmail.com
- linkedin:  <a href="https://www.linkedin.com/in/javier-gomez-del-pulgar/?locale=en_US">Javier Gómez del Pulgar</a>