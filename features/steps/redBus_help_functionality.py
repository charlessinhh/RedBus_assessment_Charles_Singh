from behave import *

from configuration.config import TestData
from helper.utils import take_screenshot
from pages.help_page import HelpPage


@given(u'User opens the redbus website')
def step_impl(context):
    try:
        context.driver.get(TestData.URL)

        #init the HELP PAGE
        context.help_page = HelpPage(context.driver)
    except Exception as e:
        take_screenshot(context.driver, 'User opens the redbus website')
        context.scenario.skip(reason=str(e))


@when(u'User clicks on help')
def step_impl(context):
    try:
        context.help_page.click_help()
    except Exception as e:
        take_screenshot(context.driver,'User clicks on help')
        context.scenario.skip(reason=str(e))


@when(u'User switches to the new window')
def step_impl(context):
    try:
        context.help_page.switch_to_new_window()
    except Exception as e:
        take_screenshot(context.driver, f"User switches to the new window")
        context.scenario.skip(reason=str(e))


@then(u'User verify the help_page_title')
def step_impl(context):
    try:
        expected_title = TestData.HELP_PAGE_TITLE
        actual_title = context.help_page.get_help_page_title()

        # Assert that the actual title matches the expected title
        assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"
    except Exception as e:
        take_screenshot(context.driver,'User verify the help_page_title')
        context.scenario.skip(reason=str(e))


@when(u'User clicks on technical issues')
def step_impl(context):
    try:
        context.help_page.click_technical_issues()
    except Exception as e:
        take_screenshot(context.driver,'User clicks on technical issues')
        context.scenario.skip(reason=str(e))


@then(u'User verify the options')
def step_impl(context):
    try:
        assert context.help_page.verify_technical_options()
    except Exception as e:
        take_screenshot(context.driver,'User verify the options')
        context.scenario.skip(reason=str(e))


@when(u'User clicks on no_buses_found')
def step_impl(context):
    try:
        context.help_page.click_no_buses_found()
    except Exception as e:
        take_screenshot(context.driver,'User clicks on no_buses_found')
        context.scenario.skip(reason=str(e))


@then(u'User verify the suggestions')
def step_impl(context):
    try:
        expected_suggestions_message  = TestData.suggestions_message
        actual_suggestions_message = context.help_page.get_suggestions()
        # Assert that the actual suggestions_message  matches the expected suggestions_message
        assert actual_suggestions_message == expected_suggestions_message, f"Expected title '{expected_suggestions_message}' but got '{actual_suggestions_message}'"
    except Exception as e:
        take_screenshot(context.driver, 'User verify the suggestions')
        context.scenario.skip(reason=str(e))
