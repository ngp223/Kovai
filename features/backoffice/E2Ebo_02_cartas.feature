Feature: Cartas

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear, modificar y borrar una carta
    Then accedo a cartas
    And creo una nueva carta
    And la carta aparece en el listado
    And edito la carta creada
    And modifico la descripción de la carta con "menu modificado" y la fecha
    And guardo los cambios de la carta
    And confirmo la modificación de la carta
    And borro la carta creada
    And la carta no aparece en el listado