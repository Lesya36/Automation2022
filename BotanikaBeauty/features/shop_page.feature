@wip
Feature: New product page and quickshop functionality

  Background:
    Given Botanika Beauty shop page is launched


  Scenario Outline:Customer can purchase new product by adding "<supply>" to cart
    Given customer has selected available "<supply>" from new product page
    When  one  "<supply>" was added to the shopping cart
    Then  "<supply>" is in the cart


      Examples:
      |supply     |
      |shampoo    |
      |conditioner|
      |trio bundle|
      |spray      |


    Scenario Outline: Customer can add products to cart with quickshop option
    Given customer is on new product page
    When  clicks quickshop option on "<supply>" product
    And   selects a "<quantity>"
    Then  verify "<supply>" is in the cart

      Examples:
      |quantity   |supply     |
      |1          |shampoo    |
      |3          |conditioner|
      |           |trio bundle|
      |           |spray      |



