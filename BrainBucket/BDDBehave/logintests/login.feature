@wip
Feature: Login functionality
  Background:
    Given User launch login page


Scenario Outline: User cannot login in without entering "<credentials>" in field
   Given user is not logged in
   When user types "<credentials>" in field
   And user clicks Login button
   Then warning is shown 'No match for E-Mail Address and/or Password'

   Examples:
      | credentials |
      | email       |
      | password    |

