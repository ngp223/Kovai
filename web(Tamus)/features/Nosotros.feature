Feature: [NOSOTRO] I revise the Nosotros Page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies

@Nosotros
  Scenario: [NOS_01] Nosotros
    When I click to nosotros
    Then I see page nosotros
    And I request call