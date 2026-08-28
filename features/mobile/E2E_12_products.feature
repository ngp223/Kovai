 @E2E
 Feature: Productos

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    Then accedo a los productos
    And creo un producto
    And el producto aparece listado
    And modifico ese producto
    And el producto modificado aparece listado
    And elimino el producto