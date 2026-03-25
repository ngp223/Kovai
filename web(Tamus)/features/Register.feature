Feature: [REGISTR] Register

Background: Start
    Given I visit the main page in web
    And I click register to Web
    And I accept cookies

@Register
  Scenario: [REG_01] I do the register
    Then Do register


