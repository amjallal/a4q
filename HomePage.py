import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    close_cookie_button_selector = (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
    humberger_button_selector = (By.CSS_SELECTOR, '#data-rayons')
    epicerie_salee_selector = (By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")
    pates_riz_selector = (By.CSS_SELECTOR, "#data-menu-level-1_R13 li:nth-child(7)")
    pates_selector = (By.CSS_SELECTOR, "#data-menu-level-2_R12F05 li:nth-child(3)")
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)

    def close_cookie(self):
        close_cookie_button = self.wait.until(EC.element_to_be_clickable(self.close_cookie_button_selector))
        close_cookie_button.click()
        self.wait.until(EC.invisibility_of_element(close_cookie_button))

    def open_menu(self):
        humberger_button = self.wait.until(EC.element_to_be_clickable(self.humberger_button_selector))
        humberger_button.click()


    def open_epicerie_salee(self):
        epicerie_salee_menu = self.wait.until(EC.visibility_of_element_located(self.epicerie_salee_selector))
        self.action.move_to_element(epicerie_salee_menu)
        self.action.perform()

    def open_pates_riz(self):
        #time.sleep(2)
        pates_riz = self.wait.until(EC.visibility_of_element_located(self.pates_riz_selector))
        self.action.move_to_element(pates_riz)
        self.action.perform()

    def click_pates(self):
        pates = self.wait.until(EC.element_to_be_clickable(self.pates_selector))
        pates.click()
        self.wait.until(EC.invisibility_of_element(pates))


