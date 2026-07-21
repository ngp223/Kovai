Feature: Productos

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear un nuevo producto

    Then accedo a productos
    # And creo un nuevo producto (error, internal server error)
    # And el producto aparece en el listado
    And modifico el producto
    And restablezco el producto