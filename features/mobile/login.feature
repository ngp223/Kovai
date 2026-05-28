Feature: Login en app móvil Kova POS

  Scenario: Login correcto
    Given la app está abierta
    When introduzco email "admin@demo.com"
    And introduzco password "admin123"
    And pulso activar terminal
    Then entro en la app