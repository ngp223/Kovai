@E2E
Feature: Usuarios 
# El usuario no se crea
  Background:
    Given la app está abierta
    And el usuario "admin" está logueado en el POS

  Scenario: Crear, modificar y eliminar un usuario
    When accedo a usuariostab
    Then creo un nuevo usuariotab
    #And el usuariotab aparece en el listado
    #And modifico el usuariotab
    #And compruebo el rol personalizado del usuariotab
    #And elimino el usuariotab
    #And el usuario no aparece en el listadotab
