 @E2E
 Feature: Categorías

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    Then accedo a los modificadores
    And creo un modificador
    And el modificador aparece listado
    And modifico el modificador
    And el modificador modificado aparece listado
    And elimino el modificador
