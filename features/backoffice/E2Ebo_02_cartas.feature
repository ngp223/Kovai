Feature: Menus

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear una nueva carta
    Then accedo a cartas
    And creo una nueva carta
    And la carta aparece en el listado
