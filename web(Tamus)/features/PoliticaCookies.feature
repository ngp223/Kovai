Feature: [POLCOOK] I revise the Política Cookies
Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies

@PolCookies
  Scenario: [PCO_01] Politica Cookies
    When  I click to politica cookies
    Then I see page politica cookies
    And I request call




