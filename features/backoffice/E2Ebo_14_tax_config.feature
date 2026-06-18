Feature: Configuración Fiscal

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Acceder a Configuración Fiscal
    Then accedo a configuración fiscal
    And estoy en la página de configuración fiscal