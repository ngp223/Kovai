Feature: Categorías

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear una nueva categoría

    Then accedo a categorías
    And creo una nueva categoría
    And la categoría aparece en el listado