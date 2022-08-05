import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_ajout_produit_panier_xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    cookie = driver.find_element(By.XPATH, "//div[@class='banner-actions-container']/button")
    cookie.click()
    # time.sleep(2)
    barre_recherche = driver.find_element(By.XPATH, "//div[@class='pl-input-text']/input")
    barre_recherche.send_keys("1664" + Keys.ENTER)
    first_item = driver.find_element(By.XPATH, "//a[@href='/p/biere-lager-blonde-sans-alcool-1664-3080216055442']")
    first_item.click()
    add_product = driver.find_element(By.XPATH, "//button[@aria-label='ACHETER']/span/span")
    add_product.click()


def test_ajout_produit_panier_css():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    cookie = driver.find_element(By.CSS_SELECTOR,
                                 "div.banner-actions-container > button")  # .banner-actions-container > button
    cookie.click()
    # time.sleep(2)
    barre_recherche = driver.find_element(By.CSS_SELECTOR, "div.pl-input-text > input")  # input[required] or [required]
    # barre_recherche.send_keys("1664" + Keys.ENTER)
    barre_recherche.send_keys("1664")
    button_research = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")  # ou [type=submit]
    button_research.click()
    # first_item = driver.find_element(By.CSS_SELECTOR, "[href='/p/biere-lager-blonde-sans-alcool-1664-3080216055442']") # ce n'est pas efficase
    first_item = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_item.click()
    # add_product = driver.find_element(By.CSS_SELECTOR, "[aria-label='ACHETER'] > span > span") #[aria-label='ACHETER'] marche aussi mais ce n'est pas efficase si la langue change
    time.sleep(2)
    add_product = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    add_product.click()


def test_css_correction():
    driver = webdriver.Chrome()

    #driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    #time.sleep(2)
    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()
    #close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    #close_cookies.click()
    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()
    #time.sleep(1)
    buy_button = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")))
    #buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()
    #time.sleep(2)
    retrait_en_magasin = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    #retrait_en_magasin = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()


def test_css_correction1():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()

    buy_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    retrait_en_magasin = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()
