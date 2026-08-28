@E2E
Feature: Categorías

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    When accedo a las categorías
    Then creo una categoría
    And creo el rol
    And la categoría aparece listada
    And modifico la categoría creada
    And la categoría modificada aparece listada
    And elimino esa categoría
    And elimino el rol creado


