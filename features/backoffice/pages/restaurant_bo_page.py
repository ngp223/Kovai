from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RestaurantPage_bo:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_restaurant(self, restaurant_name):

        restaurant = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, f'//android.widget.TextView[@text="{restaurant_name}"]')
            )
        )
        restaurant.click()