Feature: Validate the help functionality

  Scenario: validate the help functionality and technical issues
    Given User opens the redbus website
    When User clicks on help
    When User switches to the new window
    Then User verify the help_page_title
    When User clicks on technical issues
    Then User verify the options
    When User clicks on no_buses_found
    Then User verify the suggestions


