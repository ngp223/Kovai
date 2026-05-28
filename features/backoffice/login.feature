Feature: Login tablet

  Scenario: Login correcto

    Given que abro el login
    When hago login con credenciales válidas
    Then entro al dashboard