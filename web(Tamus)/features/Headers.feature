Feature: [HEADERS] I revise Header

Background: Start
    Given I visit the main page in web
    And I click register to Web
    And I accept Cookies

@Header
  Scenario: [HEAD_01] Header
    When I click header usuarios
    Then I see header usuarios
    And I see header servicios
    And I see rest of the items

@HeaderUsers
  Scenario: [HEAD_02] Header:Users
   When I click header usuarios
   Then I see header usuarios

@HeaderServices
  Scenario: [HEAD_03] Header:Services
   When I click header servicios
   Then I see header servicios
