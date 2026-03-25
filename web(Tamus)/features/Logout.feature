# Created by mshi0 at 23/02/2024
@TamusWeb
Feature: [LOGOUT_] I logout from Home

  Background: I am logged as an user
    Given I visit the main page in web
    Then I login as an user

@Logout
  Scenario: [LOGOUT_01] I logout from Home
    Given I see the Home user page
    When I click on logout
    Then I see the Login page