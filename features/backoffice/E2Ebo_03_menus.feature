Feature: Menús

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear y borrar un menú
    Then accedo a menus
    And creo un nuevo menu
    And el menu aparece en el listado
    And borro el menu creado
    And el menu no aparece en el listado