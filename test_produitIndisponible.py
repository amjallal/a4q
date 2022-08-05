import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



def openProduct(driver, index):
    liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) h2")
    liste_produits[index].click()



def test_produitIndisponible():

    # Open browser and go to Web page
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    # Definition of explicit wait
    wait = WebDriverWait(driver, 10)

    # close cookies
    close_cookies_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    # Click on humberger button
    button_menu_principal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#data-rayons')))
    button_menu_principal.click()

    # Mouse over (hover) Epicerie salée
    epicerie_salee_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")))
    action = ActionChains(driver)
    action.move_to_element(epicerie_salee_menu)
    action.perform()

    # Mouse over pates, riz etc ...
    pates_riz_etc = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#data-menu-level-1_R12 li:nth-child(7)")))
    action.move_to_element(pates_riz_etc)
    action.perform()

    # Clic on Pates
    pates = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#data-menu-level-2_R12F05 li:nth-child(3)")))
    pates.click()

    # Call function to open a product
    openProduct(driver, 3)

    # wait a bit till the button acheter appears
    time.sleep(2)

    # clic on the boutton acheter
    button_acheter = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#data-produit-acheter > button")))
    button_acheter.click()

    # choose drive method
    choix_drive = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Choisir Drive']")))
    choix_drive.click()

    # write the adress
    code_postal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='pl-input-text'] [placeholder='Ex: 75014']")))
    code_postal.send_keys("75001")
    time.sleep(2)
    code_postal.send_keys(Keys.ENTER)

    # choose the city
    choix_city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Choisir le Retrait en magasin, magasin City Paris Richelieu']")))
    choix_city.click()

    # Verifier Produit Indisponible
    Indisponible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".missing-products__top-title > div:nth-child(1)")))
    assert Indisponible.text == '1 produit indisponible dans ce magasin.'

    # Take a screenshot
    driver.get_screenshot_as_file("C:\\Users\\ib\\Downloads\\Screenshots\\capture.png")
    driver.quit()

    #driver.get_screenshot_as_file("C:\\Users\\ib\\Downloads\\Screenshots\\capture.png")
    #choix_drive = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='1444']")))
    #code_postal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder = 'Ex: 75014']")))
    #code_postal = driver.find_element(By.CSS_SELECTOR, "div.suggestions-input input")
    #code_postal1 = wait.until(EC.element_to_be_clickable(code_postal))
    #time.sleep(2)