Feature: Error messages during registration process

  Scenario Outline: enter in "<field>" "<type>" value
    Given user on the registration page
    When user types "<value>" in "<field>"
    And user clicks Continue button
    Then error is shown under "<field>" field

  Examples:
    | field       | type  | value                             |
    | first_name  | short | None                              |
    | last_name   | short | None                              |
    | first_name  | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |
    | last_name   | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |
    | phone_number| short | 12                                |
    | phone_number| long  | 123456789123456789123456789123456 |
    | password    | short | Aa1                               |
    | password    | long  | 123456789123456789aAs             |
    | email       | short | Lahjkalsabc12                     |
    | email       | long  | Labcdabcdabcdabcdmoakansn12345    |
    |address 1    | short | None                              |
    |address 1    | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |
    |city         | short | None                              |
    |city         | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |