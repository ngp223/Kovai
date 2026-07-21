Feature: Promociones

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear, modificar y borrar una promoción

    Then accedo a promociones
    And creo una nueva promoción
    And la promoción aparece en el listado
    And modifico la promoción creada
    And borro la promoción creada
    And la promoción no aparece en el listado