import time

from selenium import webdriver

from ProductCategoryPage import ProductCategoryPage
from HomePage import HomePage
from ProductPage import ProductPage


def test_page_object():
    # Open browser and go to carrefour page
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    # close cookie popup -> open the menu -> put the mouse over epicerie salée -> mouse over pates'riz etc ... -> click on pates
    home = HomePage(driver)
    home.close_cookie()
    home.open_menu()
    home.open_epicerie_salee()
    home.open_pates_riz()
    home.click_pates()

    # click on the 4th product
    product_category_page = ProductCategoryPage(driver)
    product_category_page.open_product(4)

    # buy the chosen product -> select drive method -> enter the zip code -> select the first store
    # -> get the information about the product's availability
    product_page = ProductPage(driver)
    product_page.buy()
    product_page.choose_drive()
    product_page.enter_zip_code()
    product_page.select_first_store()
    #check_availabilty = product_page.get_availability_status()
    expected_result = '1 produit indisponible dans ce magasin.'
    # Verify that the product is not available
    assert product_page.get_availability_status() == expected_result

    # Take a screenshot
    time.sleep(1)
    driver.get_screenshot_as_file("C:\\Users\\ib\\Downloads\\Screenshots\\capture1.png")

    # close the navigator
    driver.quit()