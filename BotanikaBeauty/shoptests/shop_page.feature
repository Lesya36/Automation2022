@wip
Feature: Test product page and add to cart functionality

         Background:
         Given User launched Botanika shop page

      Scenario Outline: As I user I want to "<shop>" by adding "<product>" to cart
       Given I choose a random "<product>" from "<shop>" page
       When I add random quantity of the "<product>" to the shopping cart
       Then I see that number of products in the cart was updated


      Examples:
      |shop       |product    |
      |new product|shampoo    |
      |all product|conditioner|
      |quickshop  | cream     |
      |           | mouse     |
      |           | gel       |
      |           | spray     |
      |           | serum     |
      |           | mask      |
      |           | treatment |
      |           | gift card |
      |           | t-shirt   |