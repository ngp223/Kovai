Feature: Historial de Cierres

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Acceso al historial de cierres

    When accedo al historial de cierres
    Then veo el cierre en el historial

