import logging

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from configuration.config import TestData
from helper.utils import take_screenshot


# def before_all(context):
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     logging.info("Starting test run")
#     print("This is a print statement in before_all")
#
#
# def before_feature(context, feature):
#     logging.info(f"Starting feature: {feature.name}")
#     print(f"Starting feature: {feature.name}")


def before_scenario(context, scenario):
    logging.info(f"Starting scenario: {scenario.name}")
    print(f"Starting scenario: {scenario.name}")
    # Create an instance of ChromeOptions
    chrome_options = Options()

    # Disable notifications
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    context.driver = webdriver.Chrome(options=chrome_options)
    logging.info("Initialized Chrome WebDriver")
    # context.driver.get(TestData.URL)


def after_scenario(context, scenario):
    logging.info(f"Finished scenario: {scenario.name}")
    print(f"Finished scenario: {scenario.name}")
    time.sleep(15)
    if context.driver:
        context.driver.quit()



# def after_feature(context, feature):
#     logging.info(f"Finished feature: {feature.name}")
#     print(f"Finished feature: {feature.name}")
#
#
# def after_all(context):
#     logging.info("Finished test run")
#     print("Finished test run")


# Behave hook to take screenshot if step fails
# def after_step(context, step):
#     if step.status == "failed":
#         step_name = step.name
#         if context.driver:
#             take_screenshot(context.driver, step_name)