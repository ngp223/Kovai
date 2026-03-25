Feature: [COMOFUN] I revise the Como Funciona Page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies

@ComoFunciona
  Scenario: [COMOFUN_01] Como Funciona
    When I click to como funciona
    Then I see page como funciona
    And I request call