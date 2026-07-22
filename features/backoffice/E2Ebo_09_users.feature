Feature: Usuarios

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear, modificar y eliminar un usuario

    Then accedo a usuarios
    And creo un nuevo usuario
    And el usuario aparece en el listado
    And modifico el usuario
    And elimino el usuario
    And el usuario no aparece en el listado