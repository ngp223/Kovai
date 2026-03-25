Feature: [USUGRES] I revise the page

Background: I am logged as an user
    Given I visit the main page in web
    Then I login as an user

@see_restaurante
  Scenario: [USUGRES_SEE] Ver pagina principal de restaurantes
    When I click to gestion restaurantes
    Then I see gestion de restaurantes

@lateralMR
  Scenario: [USUGRES_LMA] Menu lateral de restaurantes
    When I click to gestion restaurantes
    Then I see menu lateral de restaurantes
  
@manageGR
  Scenario: [USUGRES_MNG] Gestionar restaurantes
    When I click to gestion restaurantes
    Then I manage restaurantes