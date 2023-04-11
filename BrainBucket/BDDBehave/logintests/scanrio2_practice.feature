#second practice scenario

@LoginFeature
Feature: Login into Facebook profile

Background:
Given user is at the Login Page
Scenario: Successful Login using valid credentials
  #  The user should be knowing the credentials

When user login with valid credentials
Then user should be successfully logged in
And navigated to Facebook home page

Scenario: Error Message while using Invalid Credentials
When user try to login with invalid credentials
Then an error message should be displayed
And user is redirected to login page

