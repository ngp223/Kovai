Feature: [AVISLEG] I revise the Aviso Legal

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies

@AvisoLegal
  Scenario: [AVILEG_01] Aviso Legal
    When  I click to aviso legal
    Then I see page aviso legal
    And I request call





