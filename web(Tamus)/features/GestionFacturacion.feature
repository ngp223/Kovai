Feature: [USUGFAC] I revise the page

Background: I am logged as an user
    Given I visit the main page in web
    Then I login as an user

@see_facturacion
  Scenario: [USUGFAC_SEE] Ver la pagina de gestion de facturacion
    When I click to gestion facturacion
    Then I see gestion de facturacion

@lateralMF
  Scenario: [USUGFAC_ML] Menu lateral de facturacion
    When I click to gestion facturacion
    Then I see menu lateral facturacion

@manageGF
  Scenario: [USUGFAC_MNG] Gestionar la facturacion
    When I click to gestion facturacion
    Then I manage facturacion

@validate_FNC
  Scenario: [USUGFAC_VNC] Validar el formulario de nuevo cliente
    When I click to gestion facturacion
    Then I validate the form new client

@fill_FNCM
  Scenario: [USUGFAC_FNC01] Crear un cliente con campos obligatorios
    When I click to gestion facturacion
    Then I fill in the mandatory fields in the form new client
    And I save the new client
    And I search and delete the new client

@fill_FNC
  Scenario: [USUGFAC_FNC02] Crear un cliente con todos los campos
    When I click to gestion facturacion
    Then I fill in the mandatory fields in the form new client
    And I fill in rest of fields in the form new client
    And I save the new client
    And I search and delete the new client

@search_client
  Scenario: [USUGFAC_SeC_01] Buscar un cliente
    When I click to gestion facturacion
    Then I search a client

@export_GF
  Scenario: [USUGFAC_GFEXP] Exportar un cliente
    When I click to gestion facturacion
    Then I export clients
    And I open clients file

@advance_page
  Scenario: [USUGFAC_AvP_01] Avanzar pagina del listado
    When I click to gestion facturacion
    Then I advance page facturacion

@turnback_page
  Scenario: [USUGFAC_ReP_01] Retroceder pagina del listado
    When I click to gestion facturacion
    Then I turn back page facturacion