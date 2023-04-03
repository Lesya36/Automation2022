Feature: Google search shopping
  A user can search on Google for summer dresses by color

  Background:
    Given user launched google search page

    Scenario Outline: user is searching for "<color>" dress
      When the search phrase "<color>" summer dress is entered
      Then Results of all "<color>" dresses are shown

      Examples:
      |color|
      |pink |
      |blue |

