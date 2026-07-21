from selenium.webdriver.common.by import By
from features.backoffice.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductsPage_bo(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    PRODUCTS_MENU=(By.XPATH,"//*[@id='root']/div/div/aside/nav/a[4]")
    DESCRIPCION_INPUT=(By.XPATH,"//input[@placeholder='Ej: Café con leche']")
    GUARDAR_BTN=(By.XPATH,"//button[@type='submit' and text()='Guardar']")
    OVERLAY=(By.XPATH,"//div[contains(@class,'_overlayVisible')]")

    def open_products(self):
        self.click(self.PRODUCTS_MENU)

    def edit_product(self,nombre_producto,nueva_descripcion):
        producto=(By.XPATH,f"//*[normalize-space(text())='{nombre_producto}']")
        elemento=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(producto))
        fila=elemento.find_element(By.XPATH,"ancestor::*[.//button[@title='Editar']][1]")
        boton_editar=fila.find_element(By.XPATH,".//button[@title='Editar']")
        try:
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(self.OVERLAY))
        except:
            pass
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",boton_editar)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(boton_editar))
        boton_editar.click()
        self.fill(self.DESCRIPCION_INPUT,nueva_descripcion)
        boton=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.GUARDAR_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'end'});",boton)
        time.sleep(1)
        boton.click()