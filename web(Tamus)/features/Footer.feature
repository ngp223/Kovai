Feature: [FOOTER_] I revise the Footer

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies

@Footer
  Scenario: [FOOT_01] Footer
    Then I click the footer aviso legal
    And I click the footer politica cookies
    And I click the footer politica privacidad

@AjustesCookies
  Scenario: [FOOT_02] Ajustes
    When I click the ajustes cookies
    Then I see the ajustes cookies
