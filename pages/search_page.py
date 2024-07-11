from selenium.webdriver.common.by import By

from helper.base_page import BasePage
from helper.locators import Locators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def enter_from_source(self, send_text):
        self.send_keys(send_text, *self.locators.get_locator('src_input'))

    def select_source(self, src):
        src_locator = self.locators.get_locator('src')
        self.wait_for_element_visibility(src_locator)
        all_source_name = self.find_elements(*src_locator)
        all_source_text = [element.text for element in all_source_name]
        for element_name in all_source_text:
            if element_name == src:
                self.click(*self.locators.get_locator(src))
        # print(len(all_source_name))

    def enter_to_destination(self, send_text):
        self.send_keys(send_text, *self.locators.get_locator('dest_input'))

    def select_destination(self, dest):
        dest_locator = self.locators.get_locator('dest')
        self.wait_for_element_visibility(dest_locator)
        all_dest_name = self.find_elements(*dest_locator)
        all_dest_text = [element.text for element in all_dest_name]
        for element_name in all_dest_text:
            if element_name == dest:
                self.click(*self.locators.get_locator(dest))
        # print(len(all_dest_name))

    def click_calendar(self):
        self.click(*self.locators.get_locator('calendar'))

    def select_travel_date(self, travel_date):
        date_locator = self.locators.get_date_locator(travel_date)
        self.click(*date_locator)

    def click_search_button(self):
        self.click(*self.locators.get_locator('search_button'))

    def click_pop_up(self):
        self.wait_for_element_visibility(self.locators.get_locator('pop_up'))
        ok_button = self.find_element(*self.locators.get_locator('ok_button'))
        self.scroll_and_click(ok_button)

    def sort_buses_by_departure_time(self):
        self.click(*self.locators.get_locator('departure_sort'))

    def filter_bus_type_sleeper(self):
        self.click(*self.locators.get_locator('sleeper_filter'))


    def bus_found_displayed(self):
        total_buses_text = self.get_text(*self.locators.get_locator('total_bus_count'))
        print(f"total_buses_text {total_buses_text}") #120 buses
        import re
        total_bus_count = int(re.search(r'(\d+) Buses', total_buses_text).group(1))
        return total_bus_count

    def bus_found_message_displayed(self):
        # scroll to last to get all the bus list
        self.infinite_scroll_to_page_end()

        showing_buses_elements = self.find_elements(*self.locators.get_locator('buses_count'))  # 2
        showing_buses_count_text = [element.text for element in showing_buses_elements]
        print(f"showing_buses_count_text {showing_buses_count_text}")  # ['117 buses', '3 buses']
        # Extract integer values and calculate the sum
        total_buses_displayed = sum(int(s.split()[0]) for s in showing_buses_count_text)

        self.scroll_to_top()
        return total_buses_displayed

    def get_min_fare_by_sort(self):
        #it will return first fare as text after click on sort by fare
        self.click(*self.locators.get_locator('fare_sort'))
        return int(self.get_text(*self.locators.get_locator('bus_rates')).replace("INR", "").strip())

    def get_min_fare_from_list_of_fares(self):
        # get all fares in list
        bus_rate_elements = self.find_elements(*self.locators.get_locator('bus_rates'))
        bus_rates = [element.text for element in bus_rate_elements]
        numeric_rates = []
        for rate in bus_rates:
            numeric_value = int(rate.replace('INR', '').strip())
            numeric_rates.append(numeric_value)

        # Find the  minimum rates of busess
        min_rate = min(numeric_rates)
        return min_rate


    def get_max_fare_by_sort(self):
        #it will return first fare as text after click on sort by fare
        self.click(*self.locators.get_locator('fare_sort'))
        return int(self.get_text(*self.locators.get_locator('bus_rates')).replace("INR", "").strip())


    def get_max_fare_from_list_of_fares(self):
        # get all fares in list
        bus_rate_elements = self.find_elements(*self.locators.get_locator('bus_rates'))
        bus_rates = [element.text for element in bus_rate_elements]
        numeric_rates = []
        for rate in bus_rates:
            numeric_value = int(rate.replace('INR', '').strip())
            numeric_rates.append(numeric_value)

        # Find the  maximum rates of bus fare
        max_rate = max(numeric_rates)
        return max_rate

    def verify_last_available_timing(self):
        dept_time_elements = self.find_elements(*self.locators.get_locator('dept_time'))
        bus_dept_time = [element.text for element in dept_time_elements]
        # Sort departure times to find first and last available bus timings
        dept_times_sorted = sorted(bus_dept_time)
        # Last available bus timing
        last_bus_timing = dept_times_sorted[-1]
        print(f"Last Available Bus Timing: {last_bus_timing}")

    def verify_first_available_timing(self):
        dept_time_elements = self.find_elements(*self.locators.get_locator('dept_time'))
        bus_dept_time = [element.text for element in dept_time_elements]
        # Sort departure times to find first and last available bus timings
        dept_times_sorted = sorted(bus_dept_time)
        # First available bus timing
        first_bus_timing = dept_times_sorted[0]
        print(f"\nFirst Available Bus Timing: {first_bus_timing}")


    def verify_count_of_amenities(self):
        amenity_elements = self.wait_for_visibility_of_all_elements_located(self.locators.get_locator('amenities'))
        print(f"\ncount of amenity_elements: {len(amenity_elements)}")

