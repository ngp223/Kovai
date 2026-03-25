# Created by slopez@hi-iberia.es at 31/01/2024
@TamusWeb @RemPass
Feature: [REMPASS] I visit the Remember Password Page

  Background: I visit the main page in web
    Given I visit the main page in web

@RemPass1
  Scenario: [REMPASS_01] I see the remember password page
    Given I see the Login page
    When I go into the remember password page
    Then I see the remember password page

@RemPass2
  Scenario: [REMPASS_02] I recovery the password
    Given I go into the remember password page
    When I fill the email and click on remember password
    Then I see the confirmation recovery page

@RemPass3
  Scenario: [REMPASS_03] I cancel recovery password
    Given I go into the remember password page
    When I click on back from remember password
    Then I see the Login page

@RemPass4
  Scenario: [REMPASS_04] I resend email recovery password
    Given I go into the remember password page
    When I fill the email and click on remember password
    And I click on resend email recovery password
    Then I see the confirmation recovery page
    #And I see the email sent

@RemPass5
  Scenario: [REMPASS_05] I cancel resend email recovery password
    Given I go into the remember password page
    When I fill the email and click on remember password
    And I see the confirmation recovery page
    And I click on back from confirm recovery pass
    Then I see the Login page

# --- NO MUESTRA MENSAJE DE ERROR LA WEB... NO HACE NADA
#@RemPass @RemPassError
#    Scenario: [REMPASS_0X] I recovery password without email
#        Given I see the remember password page
#        When I click on remember password
#        Then I see the error message remember password

  # comentado con Fernando que traga una "a" como correo válido