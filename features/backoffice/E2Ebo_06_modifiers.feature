Feature: Modificadores

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

Scenario: Crear, modificar y eliminar un grupo de modificadores
    Then accedo a modificadores
    And creo un nuevo grupo de modificadores
    And el grupo de modificadores aparece en el listado
    And modifico el grupo de modificadores
    And elimino el grupo de modificadores
    And el grupo de modificadores no aparece en el listado