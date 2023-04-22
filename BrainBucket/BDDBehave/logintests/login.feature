@wip
Feature: Login functionality
  Background:
    Given User launch login page

@positive
  Scenario: a user can login using correct email and password
    Given User is not logged in
    When user enters email and password
    And User clicks Login button
    Then The user's profile page will be launched

@negative @enter_email
  Scenario: User can't login without entering password
    Given User is not logged in
    When User enters email
    And User clicks Login button
    Then warning is shown 'No match for E-Mail Address and/or Password'

 @negative @skip @enter_password
 Scenario: User can't login without entering email
   Given user is not logged in
   When user enters password
   And user clicks Login button
   Then warning is shown 'No match for E-Mail Address and/or Password'

 @positive @password_reset
  Scenario: User on the login page can reset password with correct email
   Given user clicks 'Forgotten Password'
     When user enters email
     And  user clicks Continue button
     Then confirmation message is shown 'An email with a confirmation link has been sent your email address'

