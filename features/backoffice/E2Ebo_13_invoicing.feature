Feature: Facturación - Series

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear nueva serie de facturación
    Then accedo a facturacion
    And accedo a series
    And creo una nueva serie