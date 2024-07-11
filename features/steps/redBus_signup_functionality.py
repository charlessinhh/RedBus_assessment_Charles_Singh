import time

from behave import *

from configuration.config import TestData
from helper.utils import take_screenshot
from pages.signup_page import SignUpPage


@given(u'User opens the redbus website for signup')
def step_impl(context):
    try:
        context.driver.get(TestData.URL)

        # init the SignUp Page
        context.signup_page = SignUpPage(context.driver)
    except Exception as e:
        take_screenshot(context.driver, 'User opens the redbus website')
        context.scenario.skip(reason=str(e))


@when(u'User clicks on account_button')
def step_impl(context):
    try:
        context.signup_page.click_account_button()
    except Exception as e:
        take_screenshot(context.driver,'User clicks on account_button')
        context.scenario.skip(reason=str(e))



@when(u'User clicks on login_signup_button')
def step_impl(context):
    try:
        context.signup_page.click_signup_button()

    except Exception as e:
        take_screenshot(context.driver,'User clicks on login_signup_button')
        context.scenario.skip(reason=str(e))


@then(u'User cancels the signup')
def step_impl(context):
    try:
        context.signup_page.click_cancel_button()
        print("user cancels the signup")
    except Exception as e:
        take_screenshot(context.driver,'User cancels the signup')
        context.scenario.skip(reason=str(e))


