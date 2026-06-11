Feature: Login

  Scenario: Login correcto

    Given abro backoffice
    When hago login con credenciales válidas
    Then entro al dashboard