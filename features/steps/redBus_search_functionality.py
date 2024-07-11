import time

from behave import *

from configuration.config import TestData
from helper.utils import take_screenshot
from pages.search_page import SearchPage


@given(u'User opens the redbus website for bus search')
def step_impl(context):
    try:
        context.driver.get(TestData.URL)

        #init the SEARCH PAGE
        context.search_page = SearchPage(context.driver)
    except Exception as e:
        take_screenshot(context.driver, 'User opens the redbus website for bus search')
        context.scenario.skip(reason=str(e))


@when(u'User enters from src "{text}"')
def step_impl(context,text):
    try:
        print(text)
        context.search_page.enter_from_source(text)
    except Exception as e:
        take_screenshot(context.driver,'User enters from src "{text}"')
        context.scenario.skip(reason=str(e))



@when(u'User selects src "{text}"')
def step_impl(context,text):
    try:
        print(text)
        context.search_page.select_source(text)
    except Exception as e:
        take_screenshot(context.driver,'User selects src "{text}"' )
        context.scenario.skip(reason=str(e))



@when(u'User enters to dest "{text}"')
def step_impl(context,text):
    try:
        print(text)
        context.search_page.enter_to_destination(text)
    except Exception as e:
        take_screenshot(context.driver,'User enters to dest "{text}"' )
        context.scenario.skip(reason=str(e))



@when(u'User selects dest "{text}"')
def step_impl(context,text):
    try:
        print(text)
        context.search_page.select_destination(text)
    except Exception as e:
        take_screenshot(context.driver, 'User selects dest "{text}"')
        context.scenario.skip(reason=str(e))





@when(u'User clicks on calendar')
def step_impl(context):
    try:
        context.search_page.click_calendar()
    except Exception as e:
        take_screenshot(context.driver,'User clicks on calendar' )
        context.scenario.skip(reason=str(e))



@when(u'User selects "{text}" from calendar')
def step_impl(context,text):
    try:
        print(text)
        context.search_page.select_travel_date(text)
    except Exception as e:
        take_screenshot(context.driver, 'User selects "{text}" from calendar')
        context.scenario.skip(reason=str(e))




@when(u'User clicks on search_button')
def step_impl(context):
    try:
        context.search_page.click_search_button()
    except Exception as e:
        take_screenshot(context.driver, 'User clicks on search_button')
        context.scenario.skip(reason=str(e))



@when(u'User clicks on pop_up_appeared')
def step_impl(context):
    try:
        context.search_page.click_pop_up()
    except Exception as e:
        take_screenshot(context.driver, 'User clicks on pop_up_appeared')
        context.scenario.skip(reason=str(e))



@when(u'User clicks on departure to sort the buses on dept_time')
def step_impl(context):
    try:
        context.search_page.sort_buses_by_departure_time()
    except Exception as e:
        take_screenshot(context.driver,'User clicks on departure to sort the buses on dept_time' )
        context.scenario.skip(reason=str(e))



@then(u'User clicks on bus type sleeper to filter the buses')
def step_impl(context):
    try:
        context.search_page.filter_bus_type_sleeper()
    except Exception as e:
        take_screenshot(context.driver, 'User clicks on bus type sleeper to filter the buses')
        context.scenario.skip(reason=str(e))



@then(u'User verify the count_of_buses_found')
def step_impl(context):
    try:
        bus_found_displayed = context.search_page.bus_found_displayed()
        bus_found_message_displayed = context.search_page.bus_found_message_displayed()
        assert bus_found_displayed == bus_found_message_displayed, f"Expected {bus_found_displayed} buses, but got {bus_found_message_displayed} buses displayed only"

    except Exception as e:
        take_screenshot(context.driver,'User verify the count_of_buses_found' )
        context.scenario.skip(reason=str(e))



@then(u'User verify the cheapest_rate')
def step_impl(context):
    try:
        # sort the buses in ascending order and get the min fare
        min_fare_by_sort = context.search_page.get_min_fare_by_sort()
        print(min_fare_by_sort)

        min_fare_from_list_of_fares = context.search_page.get_min_fare_from_list_of_fares()
        print(min_fare_from_list_of_fares)
        assert min_fare_by_sort == min_fare_from_list_of_fares, f"Expected {min_fare_by_sort} fare, but got {min_fare_from_list_of_fares} fare displayed only"
    except Exception as e:
        take_screenshot(context.driver, 'User verify the cheapest_rate')
        context.scenario.skip(reason=str(e))

    # time.sleep(10)


@then(u'User verify the costliest_rate')
def step_impl(context):
    try:
        # again sort the buses in ascending order and get the max fare
        max_fare_by_sort = context.search_page.get_max_fare_by_sort()
        print(max_fare_by_sort)

        max_fare_from_list_of_fares = context.search_page.get_max_fare_from_list_of_fares()
        print(max_fare_from_list_of_fares)
        assert max_fare_by_sort == max_fare_from_list_of_fares, f"Expected {max_fare_by_sort} fare, but got {max_fare_from_list_of_fares} fare displayed only"
    except Exception as e:
        take_screenshot(context.driver, 'User verify the costliest_rate')
        context.scenario.skip(reason=str(e))

    # time.sleep(20)


@then(u'User verify the last_available_bus_timing')
def step_impl(context):
    try:
        context.search_page.verify_last_available_timing()
    except Exception as e:
        take_screenshot(context.driver,'User verify the last_available_bus_timing' )
        context.scenario.skip(reason=str(e))



@then(u'User verify the first_available_bus_timing')
def step_impl(context):
    try:
        context.search_page.verify_first_available_timing()
    except Exception as e:
        take_screenshot(context.driver,'User verify the first_available_bus_timing' )
        context.scenario.skip(reason=str(e))



@then(u'User verify the count_of_Amenities')
def step_impl(context):
    try:
        context.search_page.verify_count_of_amenities()
    except Exception as e:
        take_screenshot(context.driver,'User verify the count_of_Amenities' )
        context.scenario.skip(reason=str(e))

