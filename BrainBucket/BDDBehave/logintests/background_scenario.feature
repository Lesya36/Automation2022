Feature: Clothes shopping
  A user can search on Google for summer dresses by color

  Background:
    Given: user launched google search page

    Scenario: User is searching for pink dress
      When: the search phrase " pink summer dress" is entered
      Then: Results of all "pink dresses" are shown

   Scenario: User is searching for blue dress
    When: the search phrase " blue summer dress" is entered
     Then: results of all" blue dresses" are shown

