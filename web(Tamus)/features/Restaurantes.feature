Feature: [RESTAUR] I revise the Restaurantes page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header usuarios

@Restaurantes
  Scenario: [RESTA_01] Restaurantes
    When I click to restaurantes
    Then I see page restaurantes
    And I request call
