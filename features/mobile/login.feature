Feature: Login POS

  Scenario: Login completo hasta producto

    Given la app está abierta
    When hago login con usuario "admin"
    And selecciono el restaurante "tamusGV"
    And selecciono el usuario "administrador"
    And introduzco el PIN de acceso
    And entro en la app
    And veo ventas
    And selecciono la mesa B1
    And selecciono 3 comensales
    Then selecciono el producto paella