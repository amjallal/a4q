import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    buy_button_selector =(By.CSS_SELECTOR, "#data-produit-acheter")
    drive_choice_selector = (By.CSS_SELECTOR, "svg[aria-label='Choisir Drive']")
    zip_code_selector = (By.CSS_SELECTOR, "[data-testid='pl-input-text'] [placeholder='Ex: 75014']")
    first_store_selector = (By.CSS_SELECTOR, "[aria-label='Choisir le Retrait en magasin, magasin City Paris Richelieu']")
    availability_text_selector = (By.CSS_SELECTOR, ".missing-products__top-title > div:nth-child(1)")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)

    def buy(self):
        #time.sleep(1)
        buy_button = self.wait.until(EC.visibility_of_element_located(self.buy_button_selector))
        buy_button.click()

    def choose_drive(self):
        #time.sleep(1)
        drive_choice = self.wait.until(EC.element_to_be_clickable(self.drive_choice_selector))
        drive_choice.click()

    def enter_zip_code(self):
        zip_code = self.wait.until(EC.visibility_of_element_located(self.zip_code_selector))
        zip_code.send_keys("75001")
        time.sleep(2)
        zip_code.send_keys(Keys.ENTER)

    def select_first_store(self):
        first_store = self.wait.until(EC.element_to_be_clickable(self.first_store_selector))
        first_store.click()

    def get_availability_status(self):
        availability_text = self.wait.until(EC.visibility_of_element_located(self.availability_text_selector))
        return availability_text.text



