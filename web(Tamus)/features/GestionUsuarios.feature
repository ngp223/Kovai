Feature: [USUGUSU] I revise the page

Background: I am logged as an user
    Given I visit the main page in web
    Then I login as an user

@lateralMU
  Scenario: [USUGUSU_LMU] Menú lateral de gestión de usuarios
    When I click to gestion usuarios
    Then I see menu lateral usuarios

@lateralMR
  Scenario: [USUGUSU_LMR] Menú lateral de roles
    When I click to gestion usuarios
    Then I see menu lateral roles

@seeGU
  Scenario: [USE] Página principal de usuarios
    When I click to gestion usuarios
    Then I see gestion de usuarios
    And I manage usuarios

@validate_FNU
  Scenario: [USUGUSU_FNU] Validar el formulario de nuevo usuario
    When I click to gestion usuarios
    Then I validate the form new user

@create_NUM
  Scenario: [USUGUSU_NUM] Creación y borrado de un usuario con campos obligatorios
    When I click to gestion usuarios
    Then I fill in the mandatory fields in the form new user
    And I delete user

@create_NU
  Scenario: [USUGUSU_NU] Creación  y borrado de un usuario con todos los campos
    When I click to gestion usuarios
    Then I fill in the form new user
    And I delete user

@edit_user
  Scenario: [USUGUSU_EDIT] Creación, edición y borrado de un usuario
    When I click to gestion usuarios
    Then I fill in the form new user
    Then I edit a user
    And I delete user

@search_GU
  Scenario: [USUGUSU_SEA] Buscar usuario
    When I click to gestion usuarios
    Then I search a user

@export_GU
  Scenario: [USUGUSU_EXP] Exportar usuarios
    When I click to gestion usuarios
    Then I export user
    And I open user exported file

@change_pwd
  Scenario: [USUGUSU_CHGPWD] Cambiar contraseña al usuario
    When I click to gestion usuarios
    Then I fill in the form new user
    And I change password
    And I delete user

@see_roles
  Scenario: [USUGUSU_SROL] Ver roles
    When I click to gestion usuarios
    Then I click roles
    And I see roles

@credel_rol
  Scenario: [USUGUSU_CDROL] Crear y borrar rol
    When I click to gestion usuarios
    And I click roles
    Then I create a rol
    And I delete a rol

@rename_rol
  Scenario: [USUGUSU_RENROL] Renombrar rol
    When I click to gestion usuarios
    And I click roles
    Then I create a rol
    And I rename a rol
    And I delete a rol

@per_rol
  Scenario: [USUGUSU_APROL] Asignar/desasignar permiso
    When I click to gestion usuarios
    And I click roles
    Then I create a rol
    And I add permission to a rol
    And I valid permission added
    And I delete a rol



