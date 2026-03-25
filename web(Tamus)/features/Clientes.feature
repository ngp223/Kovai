Feature: [CLIENTS] I revise the Clientes Page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies

@Clientes
  Scenario: [CLIENT_01] Clientes
    When I click to clientes
    Then I see page clientes
    And I request call