Feature: [TARIFAS] I revise the Tarifas Page

Background: Start
    Given I visit the main page in web
    And I click register to Web
    And I accept Cookies

@Tarifas
  Scenario: [TAR_01] Tarifas
    When I click to tarifas
    Then I see page tarifas
    And I request call
