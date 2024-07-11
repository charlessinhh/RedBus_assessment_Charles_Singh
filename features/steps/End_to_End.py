from behave import *

from configuration.config import TestData
from helper.utils import take_screenshot
from pages.help_page import HelpPage
from pages.search_page import SearchPage
from pages.signup_page import SignUpPage


@given(u'User opens the redbus website for signup and search the buses')
def step_impl(context):
    try:
        context.driver.get(TestData.URL)

        # init the SignUp Page , Search Page, Help Page
        context.signup_page = SignUpPage(context.driver)
        context.search_page = SearchPage(context.driver)
        context.help_page = HelpPage(context.driver)
    except Exception as e:
        take_screenshot(context.driver, 'User opens the redbus website for signup and search the buses')
        context.scenario.skip(reason=str(e))