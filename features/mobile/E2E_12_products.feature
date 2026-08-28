 @E2E
 Feature: Productos

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    When accedo a los productos
    Then creo un producto
    And el producto aparece listado
    And modifico ese producto
    And el producto modificado aparece listado
    And elimino el producto