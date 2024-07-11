Feature: Validate the search functionality

  @Valid_search
  Scenario Outline: Search buses with sleeper class and from given source and dest
    Given User opens the redbus website for bus search
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

    Examples:
      |from_src|src|to_dest|dest|travel_date|
      |  bang     | Bangalore |  che          |  Koyambedu  |   14         |

