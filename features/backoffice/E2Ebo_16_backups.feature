Feature: Backups

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear y eliminar una copia de respaldo
    Then accedo a backups
    And creo una copia de respaldo
    And la copia aparece en el listado
    And descargo la copia de respaldo
    And el fichero de respaldo es válido
    And elimino la copia de respaldo
    And la copia no aparece en el listado