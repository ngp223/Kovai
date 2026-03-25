Feature: [INTEGRA] I revise the Integraciones page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header servicios

@Integraciones
  Scenario: [INT_01] Integraciones
    When I click to integraciones
    Then I see page integraciones
    And I request call