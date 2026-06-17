Feature: Historial de ventas

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Exportar CSV y validar importe con pandas

    Then accedo a historial ventas
    And selecciono Tamus Rooftop Sevilla
    And exporto el CSV
    And se descarga y valido el fichero CSV