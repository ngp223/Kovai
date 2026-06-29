Feature: Mesas

  Background:
    Given la web está abierta
    When hago login con credenciales válidas

  Scenario: Crear y eliminar una mesa
    Then accedo a mesas
    And selecciono el restaurante Tamus Rooftop Sevilla
    And creo una mesa
    And la mesa aparece en el mapa
    And elimino la mesa
    And la mesa no aparece en el mapa