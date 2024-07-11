from configuration.config import TestData
from helper.base_page import BasePage
from helper.locators import Locators

class HelpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def click_help(self):
        self.click(*self.locators.get_locator('help'))

    def get_help_page_title(self):
        actual_title = self.get_text(*self.locators.get_locator('redBus_Help'))
        return actual_title

    def click_technical_issues(self):
        iframe_locator = self.locators.get_locator('iframe_help')
        self.wait_for_element_presence(iframe_locator)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_locator))
        self.click(*self.locators.get_locator('technical_issues'))

    def verify_technical_options(self):
        technical_options_locator = self.locators.get_locator('technical_options')
        self.wait_for_element_visibility(technical_options_locator)
        technical_options_elements = self.find_elements(*technical_options_locator)
        # print("options")
        technical_options = [element.text for element in technical_options_elements]
        print(f"technical_options: {technical_options}")
        return self.is_displayed(*self.locators.get_locator('technical_options'))

    def click_no_buses_found(self):
        self.click(*self.locators.get_locator('no_buses_found'))

    def get_suggestions(self):
        # suggestion_block = self.wait_for_element_visibility(self.locators.get_locator('suggestion_block'))
        suggestion_block = self.get_text(*self.locators.get_locator('suggestion_block'))
        return suggestion_block

    def switch_to_new_window(self):
        original_handle = self.get_current_window_handle()
        handles = self.get_all_window_handles()
        for handle in handles:
            if handle != original_handle:
                self.driver.switch_to.window(handle)
                break
