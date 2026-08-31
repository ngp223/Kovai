 @E2E
 Feature: Impresoras

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    When accedo a las impresoras
    Then modifico campos
    And los campos han sido modificados
    And los campos han sido restablecidos