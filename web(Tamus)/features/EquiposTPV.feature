Feature: [EQUITPV] I revise the Equipos TPV page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header servicios


@Cafeterias
  Scenario:[TPV_01] Equipos TPV
    When I click to equipos tpv
    Then I see page equipos tpv
    And I request call