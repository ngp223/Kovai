Feature: Logs - Auditoría del sistema

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Acceder a logs y paginar resultados
    Then accedo a logs
    And estoy en la página de logs
    And filtro por el restaurante Sevilla
    And voy a la siguiente página de logs
    Then se muestra un id de log