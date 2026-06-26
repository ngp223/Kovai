Feature: Soporte

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear una petición de soporte
    Then accedo a soporte
    And creo una petición de soporte
    And la petición aparece en el listado

    # Pendiente de implementación en la aplicación
    # And elimino la petición
    # And la petición no aparece en el listado