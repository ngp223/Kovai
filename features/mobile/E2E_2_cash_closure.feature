Feature: Cash Closure POS

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS
    And está en la pantalla de ventas

  Scenario: Cierre de caja completo
    When accedo al cierre de caja
    And abro normal declarado
    And copio el esperado primero
    And copio el esperado segundo
    And hago scroll hasta finalizar cierre
    Then realizo el cierre de caja
    