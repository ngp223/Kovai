Feature: Usuarios

  Background:
    Given la web está abierta
    When hago login con credenciales válidas
    
  Scenario: Consultar devices
    
    Then accedo a dispositivos
    And veo el dispositivo general
    And filtro por Tamus Rooftop Sevilla
    And veo el dispositivo del restaurante
    And vuelvo a todos los restaurantes
    And vuelvo a ver el dispositivo general