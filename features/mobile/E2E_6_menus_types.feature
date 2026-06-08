Feature: Menus

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Crear una nueva carta

    When accedo al módulo de cartas
    Then creo una nueva carta con datos válidos
