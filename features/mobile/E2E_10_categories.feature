Feature: Categorías

  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: 
    Then accedo a las categorías
    And creo una categoría
    #And creo el rol
    And la categoría aparece listada
    #And modifico la categoría creada
    #And la categoría modificada listada
    And elimino esa categoría
    And la categoría no aparece listada
    #And elimino el rol creado

