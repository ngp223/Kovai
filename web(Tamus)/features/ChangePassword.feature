@TamusWeb
Feature: [CHAPASS] I change password for a user

  Background: I am logged as an user
    Given I visit the main page in Web
    Then I login as an user

# Cambiar password
@ChangePass @ChangePassOK
  Scenario: [CHAPASS_01] I go into change password option
    Given I see the Home user page
    When I click on change password
    Then I see the change password option

@ChangePass  @ChangePassOK  # Pte tener usuario al que poder cambiarle la password
  Scenario: [CHAPASS_02] I change password
    Given I click on change password
    When I fill out all data
    And I click on confirm button
    # Then I see the confirmation message
    # And I can login with the new password

# Change password KO
@ChangePass  @ChangePassKO
  Scenario Outline: [CHAPASS_03] I change password with wrong data
    Given I click on change password
    When I fill out with <actPass> <newPass> <confNewPass> wrong data
    And I click on confirm button
    Then I see message error <msgeError>

  Examples: Data password empty
    | actPass       | newPass         | confNewPass     | msgeError                                                                                                                                           |
    | PasswordOK123 | PasswordOK123   | PasswordOK123   | La contraseña actual es incorrecta                                                                                                                  |
    | None          | None            | None            | Los campos seleccionados son obligatorios.                                                                                                          |
    | None          | PasswordOK123   | PasswordOK123   | Los campos seleccionados son obligatorios.                                                                                                          |
    | PasswordOK123 | None            | PasswordOK123   | Los campos seleccionados son obligatorios.                                                                                                          |
    | PasswordOK123 | PasswordOK123   | None            | Los campos seleccionados son obligatorios.                                                                                                          |
    | PasswordOK123 | PasswordOK123   | PasswordOK456   | Las contraseñas no concuerdan                                                                                                                       |
    | PasswordOK123 | Pass123         | Pass123         | La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&\| |
    | PasswordOK123 | passwordok123   | passwordok123   | La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&\| |
    | PasswordOK123 | Passwordok,123  | Passwordok,123  | La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&\| |
    | PasswordOK123 | Passwordok;123  | Passwordok;123  | La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&\| |
    | PasswordOK123 | Passwordok&123  | Passwordok&123  | La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&\| |
    | PasswordOK123 | Passwordok\|123 | Passwordok\|123 | La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&\| |
    | PasswordOK123 | Passwordok 123  | Passwordok 123  | La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&\| |

  @ChangePass  @ChangePassKO
  Scenario: [CHAPASS_04] I cancel the change password
    Given I click on change password
    When I fill out all data
    And I click on cancel button change password
    Then I see the Home user page

  @ChangePass  @ChangePassKO
  Scenario: [CHAPASS_05] I close the change password
    Given I click on change password
    When I fill out all data
    And I click on close change password
    Then I see the Home user page