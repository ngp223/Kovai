@E2E
Feature: Facturación

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Crear una nueva factura
    When accedo al módulo de facturación
    Then creo una nueva factura con datos válidos
    #And la factura se crea correctamente, sin hacer
    #And veo la factura en el listado de facturas, sin hacer
# da error al final de crear factura