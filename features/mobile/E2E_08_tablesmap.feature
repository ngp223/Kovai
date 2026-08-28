@E2E
Feature: Menús

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Crear un menú
    When accedo a las mesas
    Then creo tarifa
    And creo zona
    And selecciono la zona 
    And creo la mesa
    And la mesa se muestra en el mapa
    And muevo la mesa creada
    And borro la mesa creada
    And borro la zona
    And borro la tarifa
