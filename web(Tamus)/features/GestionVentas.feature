Feature: [USUGVEN] I revise the page

Background: I am logged as an user
    Given I visit the main page in web
    Then I login as an user

@see_ventas
  Scenario: [USUGALM_SEE] Ver pagina principal de almacen
    When I click to gestion ventas
    Then I see gestion de ventas

@lateral_GV
  Scenario: [USUGVEN_MLV] Menu lateral de ventas
    When I click to gestion ventas
    Then I see menu lateral ventas

@export_GV
  Scenario: [USUGVEN_EXP] Gestionar ventas
    When I click to gestion ventas
    And I select restaurant
    Then I do export ventas
    And I open ventas exported file

@search_GV
  Scenario: [USUGVEN_SEA] Gestionar ventas
    When I click to gestion ventas
    And I select restaurant
    Then I revise form advance search
    And I fill advance search

@manage_GV
  Scenario: [USUGVEN_MNG] Gestionar ventas
    When I click to gestion ventas
    And I select restaurant
    Then I manage ventas

@IP_report
  Scenario: [USUGVEN_IPR] Informes personalizados
    When I click to gestion ventas
    Then I see informes
    And I search informes
    And I do export informes
    And I open informes exported file

@IP_repper
  Scenario: [USUGVEN_IPRP] Informes personalizados
    When I click to gestion ventas
    Then I see informes personalizados
    And I search informes personalizados

@VO_report
  Scenario: [USUGVEN_VOR] Visualizacion Online
    When I click to gestion ventas
    And I select restaurant
    Then I see visual online
    And  I see VO_report

@VO_seapro
  Scenario: [USUGVEN_VOSP] Visualizacion Online
    When I click to gestion ventas
    And I select restaurant
    Then I see visual online
    And I see products
    And I search products

@VO_exppro
  Scenario: [USUGVEN_VOEP] Visualizacion Online
    When I click to gestion ventas
    And I select restaurant
    Then I see visual online
    And I see products
    And I do export products
    And I open products exported file

@VO_delres
  Scenario: [USUGVEN_VODR] Visualizacion Online
    When I click to gestion ventas
    And I select restaurant
    Then I see visual online
    And I delete restaurant






