 @E2E
 Feature: Requests

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    When accedo a peticiones
    Then creo petición
    And verifico la creación de la petición
    And modifico petición
    And verifico petición modificada
    #And borro la petición --> no se puede