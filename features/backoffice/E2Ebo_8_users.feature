Feature: Usuarios

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear un nuevo usuario

    Then accedo a usuarios
    And creo un nuevo usuario
    And el usuario aparece en el listado