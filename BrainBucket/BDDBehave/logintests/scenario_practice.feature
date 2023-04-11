@dropdowns
Feature: Zara shopping

  Scenario Outline: Show all available jeans category
    Given a web browser is at the Zara home page
    When user selects jeans from product menu
    Then all available jean "<styles>" are displayed

    Examples:
    |styles    |
    |skinny    |
    |mom fit   |
    |straight  |
    |high waist|
    |mid rise  |
    |low rise  |


