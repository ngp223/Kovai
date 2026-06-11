Feature: Menús

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Crear un menú

    When accedo al módulo de menús
    And creo un menú con datos válidos
    Then el menú se crea correctamente