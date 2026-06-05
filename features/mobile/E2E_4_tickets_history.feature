Feature: Historial de Tickets

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Acceso al historial de tickets

    When accedo al historial de tickets
    Then veo el historial de tickets

