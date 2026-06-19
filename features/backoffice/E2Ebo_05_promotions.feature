Feature: Promociones

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear una nueva promoción

    Then accedo a promociones
    And creo una nueva promoción
    And la promoción aparece en el listado