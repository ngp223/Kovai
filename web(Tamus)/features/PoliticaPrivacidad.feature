Feature: [POLPRIVA] I revise the Politica Privacidad
Background: Start
    Given I visit the main page in web
    And I click register to Web
    And I accept cookies

@PolPrivacidad
  Scenario: [PPRI_01] Politica Privacidad
    When I click to politica privacidad
    Then I see page politica privacidad
    And I request call
