Feature: Menús

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear modificar y borrar un menú
    When accedo a menus
    And creo un nuevo menu
    And modifico el menu y añado platos
    Then el menu aparece con 3 productos
    When borro el menu creado
    Then el menu no aparece en el listado
