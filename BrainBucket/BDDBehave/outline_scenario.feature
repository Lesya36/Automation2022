Feature: Airbnb login
In order to use application, I need to be logged in as a user and a host.


    Scenario Outline: login into application as a "<role>" with multi role account
        Given a web browser is on Airbnb homepage
        When "<role>" enters "<username>" and "<password>"
        Then successful login message is on the screen
        And switch between user and host profile is available

        Examples:
            | username  | password    | role |
            | lesya92   | Fluffy@98   | user |
            | rentals36 | Wisconsin85 | host |




