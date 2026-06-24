Feature: Cartas

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear y borrar una carta
    Then accedo a cartas
    And creo una nueva carta
    And la carta aparece en el listado
    And borro la carta creada
    And la carta no aparece en el listado