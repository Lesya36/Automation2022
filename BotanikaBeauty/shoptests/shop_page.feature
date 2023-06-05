@wip
Feature: Test product page and add to cart functionality

         Background:
         Given User launched Botanika Beauty shop page

      Scenario Outline:User wants to "<shop>" by adding "<product>" to cart
       Given User has selected random "<product>" from "<shop>" page
       When Random quantity of the "<product>" was added to the shopping cart
       Then User can see that number of products in the cart was updated


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