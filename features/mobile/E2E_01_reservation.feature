Feature: Reservations POS

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS
    And está en la pantalla de ventas

  Scenario: Venta completa con pago
    When selecciono la mesa "B1"
    And selecciono comensales
    And selecciono el producto
    And añado el producto al pedido
    And aumento la cantidad del producto
    And realizo el pago
    And confirmo el pago
    Then finalizo el pedido
    And salgo del modo TPV
