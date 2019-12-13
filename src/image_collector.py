import os
#como refactorizo esto?¿ tengo dos return y no quiero llamar dos veces a la funcion

def imagedir_collector(directory_root)
'''Get all the picture directories'''

    

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

                return image_directory

     except Exception as e:
        print(f"Error : {e}")