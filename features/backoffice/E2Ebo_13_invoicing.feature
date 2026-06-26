Feature: Facturación - Series

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear y eliminar una serie de facturación
    Then accedo a facturacion
    And accedo a series
#    And creo una nueva serie
#    And la serie aparece en el listado
#    And elimino la serie
#    And la serie no aparece en el listado
  #BUG CRITICAL: no se pueden borrar las series, con lo que no se crean mas