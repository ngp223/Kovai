# Created by slopez@hi-iberia.es at 18/01/2024
 
@TamusWeb
Feature: [LOGGING] I visit the Login Page

### Login OK

@Login1
  Scenario: [LOGIN_01] I login as an user
    Given I visit the main page in web
    When I see the Login page
    Then I login as an user

### Login Errors

@Login @LoginError2
  Scenario: [LOGIN_02] I try to login with wrong user
    Given I visit the main page in web
    When I see the Login page
    Then I try to login with wrong user

@Login @LoginError3
  Scenario: [LOGIN_03] I try to login with wrong password
    Given I visit the main page in web
    When I see the Login page
    Then I try to login with wrong password

#@Login @LoginError4
#  Scenario: [LOGIN_04] I try to login without user
#    Given I visit the main page in web
#    When I see the Login page
#    Then I try to login without user
 ### CODIGO MAL HECHO. SE QUEDA PILLADO,DECIRSELO A FERNANDO  ,SE VE CON NAVEGADOR EN INCOGNITO

@Login @LoginError5
  Scenario: [LOGIN_05] I try to login without password
    Given I visit the main page in web
    When I see the Login page
    Then I try to login without password



  

