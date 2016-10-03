Feature: Amazon shopping basket

  Scenario: View the shopping basket product(s)
    Given I visit a product page on amazon.com
    When I click on the Add to Cart button
    Then the product is added to the basket
    When I go to my shopping basket page
    Then I can view my product