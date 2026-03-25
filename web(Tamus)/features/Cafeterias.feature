Feature: [CAFET__] I revise the Cafeterias page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header usuarios

@Cafeterias
  Scenario: [CAFE_01] Cafeterias
    When I click to cafeterias
    Then I see page cafeterias
    And I request call
