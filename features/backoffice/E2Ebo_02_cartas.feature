Feature: Cartas

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear, modificar y borrar una carta
    Then accedo a cartas
    And creo una nueva carta
    And la carta aparece en el listado
    And cambio al restaurante "Tamus Rooftop Sevilla"
    And asigno la carta creada como carta maestra
    And la carta queda asignada
    And cierro la ventana de asignar carta
    And la carta aparece marcada por defecto
    And cambio al restaurante "Tamus Beach Club Marbella"
    And edito la carta creada
    And modifico la descripción de la carta con "menu modificado" y la fecha
    And guardo los cambios de la carta
    And confirmo la modificación de la carta
    And borro la carta creada
    And la carta no aparece en el listado
    And escaneo la carta con IA
