from helper.base_page import BasePage
from helper.locators import Locators


class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def click_account_button(self):
        self.click(*self.locators.get_locator('account_button'))


    def click_signup_button(self):
        self.click(*self.locators.get_locator('login_signup_button'))

    def click_cancel_button(self):
        self.click(*self.locators.get_locator('signup_cancel_button'))