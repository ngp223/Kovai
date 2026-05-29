Feature: Login POS

  Scenario: Login y acceso a restaurante

    Given la app está abierta
    When hago login con usuario "admin"
    And selecciono el restaurante "tamusGV"
    Then entro en la app