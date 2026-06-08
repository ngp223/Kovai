Feature: Facturación

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Crear una nueva factura

    When accedo al módulo de facturación
    And creo una nueva factura con datos válidos
# da error al final de crear factura