Feature: [HOTELES] I revise the Hoteles page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header usuarios

@Hoteles
  Scenario: [HOT_01] Hoteles
    When I click to hoteles
    Then I see page hoteles
    And I request call

