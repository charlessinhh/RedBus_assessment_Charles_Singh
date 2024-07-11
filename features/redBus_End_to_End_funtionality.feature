Feature: Validate the End to End functionality of RedBus Website

  Scenario Outline: SignUp and search for the sleeper buses on given date and use of customer help option to verify the options
    Given User opens the redbus website for signup and search the buses

    When User clicks on account_button
    When User clicks on login_signup_button
    Then User cancels the signup

    When User enters from src "<from_src>"
    When User selects src "<src>"
    When User enters to dest "<to_dest>"
    When User selects dest "<dest>"
    When User clicks on calendar
    When User selects "<travel_date>" from calendar
    When User clicks on search_button
    When User clicks on pop_up_appeared
    When User clicks on departure to sort the buses on dept_time
    Then User clicks on bus type sleeper to filter the buses
    Then User verify the count_of_buses_found
    Then User verify the cheapest_rate
    Then User verify the costliest_rate
    Then User verify the last_available_bus_timing
    Then User verify the first_available_bus_timing
    Then User verify the count_of_Amenities

    When User clicks on help
    When User switches to the new window
    Then User verify the help_page_title
    When User clicks on technical issues
    Then User verify the options
    When User clicks on no_buses_found
    Then User verify the suggestions

    Examples:
      |from_src|src|to_dest|dest|travel_date|
      |  bang     | Bangalore |  che          |  Koyambedu  |   14         |
