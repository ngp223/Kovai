@E2E
Feature: Settings

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Configurar ajustes
    When accedo a ajustes
    Then cambio el aspecto a oscuro
    And cambio el tamaño de texto a grande
    And verifico que el texto aumenta de tamaño
    And cambio el idioma a ingles
    And cierro sesión