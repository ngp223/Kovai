Feature: [BARES__] I revise the Bares page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header usuarios

@Bares
  Scenario: [BAR_01] Bares/pubs
    When I click to bares
    Then I see page bares
    And I request call


