from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductCategoryPage:

    products_selector = ".product-grid-item:not(.storetail) h2"
    #buy_button_selector = (By.CSS_SELECTOR, "#data-produit-acheter > button")
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)

    def open_product(self, index):
        product_lists = self.driver.find_elements(By.CSS_SELECTOR, self.products_selector)
        product_lists[index-1].click()
        #self.wait.until(EC.visibility_of_element_located(self.buy_button_selector))
