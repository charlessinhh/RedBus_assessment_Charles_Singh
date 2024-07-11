from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
import datetime
import allure

def get_current_window_handle(driver):

    handle = driver.current_window_handle
    print(f"handle :> {handle}")
    if handle:
        return handle
    else:
        raise Exception("no current window handle found")


def get_multiple_window_handles(driver):

    handles = driver.window_handles
    print(f"handles :> {handles}")
    if len(handles) > 1:
        return handles
    else:
        raise Exception("No multiple window handles found")


def wait_for_element_presence(driver, locator, timeout=10):

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Timed out waiting for element {locator}")


def wait_for_element_visibility(driver, locator, timeout=10):

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Timed out waiting for element {locator}")


def wait_for_element_clickable(driver, locator, timeout=10):

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Timed out waiting for element to be clickable {locator}")


def wait_for_visibility_of_all_elements_located(driver, locator, timeout=10):

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Timed out waiting for all element to be visible {locator}")

def take_screenshot(driver, step_name):
    """
    Takes a screenshot of the current browser window.

    :param driver: Selenium WebDriver instance
    :param step_name: Name of the step where the screenshot is taken
    """
    screenshots_dir = "screenshots"  # Directory to save screenshots
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_file = os.path.join(screenshots_dir, f"{step_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved: {screenshot_file}")

    # Attach screenshot to Allure report
    with open(screenshot_file, "rb") as image_file:
        allure.attach(image_file.read(), name=step_name, attachment_type=allure.attachment_type.PNG)



