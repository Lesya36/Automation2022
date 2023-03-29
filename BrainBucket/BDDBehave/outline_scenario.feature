Feature: Airbnb test
In order to use application, I need to be logged in as a user and a host.


    Scenario Outline outline: try login
        Given: a web Browser is on Airbnb homepage
        When: the following <username> and <password> is filled up
        And: successful login message is on the screen
        Then: switch between user and host profile is available

        Examples:
            | username  | password    |
            | lesya92   | Fluffy@98   |
            | rentals36 | Wisconsin85 |




