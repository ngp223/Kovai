Feature: Menús

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear un nuevo menú
    Then accedo a menus
    And creo un nuevo menu
    And el menu aparece en el listado