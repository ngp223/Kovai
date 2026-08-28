 @E2E
 Feature: Promociones

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    When accedo a las promociones
    Then creo una promoción
    And la promoción aparece listado
    And modifico la promoción
    And la promoción modificada aparece listado
    And elimino la promoción