Feature: [TAKEAWA] I revise the Take Away page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header servicios


@TakeAway
  Scenario: [TAKEA_01] Take Away
    When I click to take away
    Then I see page take away
    And I request call