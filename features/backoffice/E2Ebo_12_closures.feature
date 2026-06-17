Feature: Cierres

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Filtrar cierres por empleado

    Then accedo a cierres
    And cambio al restaurante Tamus Rooftop Sevilla
    And filtro por Maître Alberto
    And veo el cierre del empleado