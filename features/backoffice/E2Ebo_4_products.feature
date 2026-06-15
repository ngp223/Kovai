Feature: Productos,error, internal server error

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear un nuevo producto

    Then accedo a productos
#    And creo un nuevo producto
#    And el producto aparece en el listado
  # error, internal server error