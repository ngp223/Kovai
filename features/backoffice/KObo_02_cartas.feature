Feature: Validaciones Cartas

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear una carta sin nombre
    Then accedo a cartas
    And intento crear una carta sin nombre
    Then aparece el mensaje de nombre obligatorio
