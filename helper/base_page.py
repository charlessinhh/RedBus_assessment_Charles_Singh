from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper.utils import wait_for_element_clickable, wait_for_element_visibility, wait_for_element_presence, \
    get_current_window_handle, get_multiple_window_handles, wait_for_visibility_of_all_elements_located
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        element = wait_for_element_clickable(self.driver, locator)
        element.click()

    def send_keys(self, text, *locator):
        element = wait_for_element_visibility(self.driver, locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def get_text(self, *locator):
        element = wait_for_element_visibility(self.driver, locator)
        return element.text

    def is_displayed(self, *locator):
        try:
            element = wait_for_element_visibility(self.driver, locator, timeout=1)
            return element.is_displayed()
        except TimeoutException:
            return False

    def wait_for_element_presence(self, locator, timeout=10):
        return wait_for_element_presence(self.driver, locator, timeout)

    def wait_for_element_visibility(self, locator, timeout=10):
        return wait_for_element_visibility(self.driver, locator, timeout)

    def wait_for_element_clickable(self, locator, timeout=10):
        return wait_for_element_clickable(self.driver, locator, timeout)

    def wait_for_visibility_of_all_elements_located(self, locator, timeout=10):
        return wait_for_visibility_of_all_elements_located(self.driver, locator, timeout)

    def get_current_window_handle(self):
        return get_current_window_handle(self.driver)

    def get_all_window_handles(self):
        return get_multiple_window_handles(self.driver)

    def scroll_and_click(self, element):
        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Click the "Ok, got it" button using JavaScript
        self.driver.execute_script("arguments[0].click();", element)

    def infinite_scroll_to_page_end(self):
        # Scroll to the end of the page to get all the rates
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new content to load
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def scroll_to_top(self):
        # Scroll to the top of the page
        self.driver.execute_script("window.scrollTo(0, 0);")

        # Optionally, you can add a wait to see the effect
        import time
        time.sleep(2)