# Created by Owner3010 at 11/8/2024
Feature: Target Gifts

  Background:
    Given Navigate to https://www.target.com/

  Scenario: Navigate to the page
#    Given Navigate to https://www.target.com/

  Scenario: Search for gifts
#    Given Navigate to https://www.target.com/
    When Search for Gift Ideas

  Scenario Outline: Verify searched page's headers
#    Given Navigate to https://www.target.com/
    When Search for <search_item>
    Then Verify header of the page contains <search_item>

    Examples:
      | search_item |
      | Gift Ideas  |
#      | iphone      |


