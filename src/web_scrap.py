from selenium import webdriver
from selenium.webdriver.support.ui import Select

def get_ai(crop,disease):

'''Use selenium for getting an excel with the avialable ai for fighting the specified disease'''

    crop_code = {'tomato':'0104010401010000','pepper_bell':'0104010401020000','grape':'0102020600000000'}
    disease_code = {'septoria_leaf_spot':'275','bacterial_spot':'666','alternaria_early_blight':'11','phytopthora_late_blight': '937',
    'mosaic_virus':'754','black_rot':'233','black_measles':'441','bacteria_spot_pepper':'417'}


    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://www.mapa.gob.es/es/agricultura/temas/sanidad-vegetal/productos-fitosanitarios/registro/productos/conaplipla.asp')

    #dropdown
    ambito_dropdown =  Select(driver.find_element_by_name('ambUti'))
    ambito_dropdown.select_by_index(1)
    consultar_button = driver.find_element_by_name('bt_matr1').click()

    cultivo_dropdown = Select(driver.find_element_by_name('culUso'))
    cultivo_dropdown.select_by_value(crop_code[crop])
    consultar_button = driver.find_element_by_name('bt_matr1').click()

    disease_dropdown = Select(driver.find_element_by_name('plagEfecto'))
    disease_dropdown.select_by_value(disease_code[disease])
    consultar_button = driver.find_element_by_name('bt_matr1').click()

    #get excel file
    get_excel_button = driver.find_element_by_name('cd_matr').click()
    download_excel = driver.find_element_by_css_selector('div:nth-child(8) > ul > li > a').click()

    return f'Excel file ready for {crop} {disease}!'
