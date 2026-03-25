Feature: [EVENTOS] I revise the Eventos page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header usuarios

@Eventos
  Scenario:[EVE_01] Eventos
    When I click to eventos
    Then I see page eventos
    And I request call
