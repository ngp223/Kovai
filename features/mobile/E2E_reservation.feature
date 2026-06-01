Feature: Login POS

  Scenario: Venta completa con pago

    Given la app está abierta
    When hago login con usuario "admin"
    And selecciono el restaurante "tamusGV"
    And selecciono el usuario "administrador"
    And introduzco el PIN de acceso
    And entro en la app
    And veo ventas
    And selecciono la mesa "B1"
    And selecciono comensales
    Then selecciono el producto
    And añado el producto al pedido
    And aumento la cantidad del producto
    And realizo el pago
    And confirmo el pago
    And finalizo el pedido