@wip
Feature: Test new product page and quickshop functionality

  Background:
    Given Botanika Beauty shop page is launched


  Scenario Outline:Customer can purchase new product by adding "<supply>" to cart
    Given customer has selected available "<supply>" from new product page
    When  "<quantity>" of the "<supply>" was added to the shopping cart
    Then customer can see that number of products in the cart was updated


      Examples:
      |quantity   |supply     |
      |1          |shampoo    |
      |3          |conditioner|
      |5          |trio bundle|
      |           |spray      |


    Scenario Outline: Customer can add products to cart with quickshop option
    Given customer is on new product page
    When  customer clicks quickshop option on "<supply>" product
    And   one "<supply>" was added to the cart
    Then  verify that product in the cart was updated

      Examples:
      |supply     |
      |shampoo    |
      |conditioner|
      |trio bundle|
      |spray      |




