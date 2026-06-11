Feature: Login

  Scenario: Login correcto
    Given la web está abierta
    When hago login con credenciales válidas
    Then entro al panel de control