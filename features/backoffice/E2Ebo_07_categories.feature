Feature: Categorías

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear y eliminar una categoría
    Then accedo a categorías
    And creo una nueva categoría
    And la categoría aparece en el listado
    And elimino la categoría
    And la categoría no aparece en el listado