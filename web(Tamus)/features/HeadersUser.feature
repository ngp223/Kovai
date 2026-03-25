
Feature: [HEADERU] I revise the Header_user

Background: I am logged as an user
    Given I visit the main page in web
    Then I login as an user

@HeadersUserRestaurantes
  Scenario: [HEADUS_01] HeadersUser Restaurantes
    When I click to gestion restaurantes
    Then I see gestion de restaurantes

@HeadersUserAlmacen
  Scenario: [HEADUS_02] HeadersUser Almacen
    When I click to gestion almacen
    Then I see gestion de almacen

@HeadersUserVentas
  Scenario: [HEADUS_03] HeadersUser Ventas
    When I click to gestion ventas
    Then I see gestion de ventas

@HeadersUserFacturacion
  Scenario: [HEADUS_04] HeadersUser Facturacion
    When I click to gestion facturacion
    Then I see gestion de facturacion

@HeadersUserUsuarios
  Scenario: [HEADUS_05] HeadersUser Usuarios
    When I click to gestion usuarios
    Then I see gestion de usuarios
