@TamusWeb
Feature: [NOTIFIC] I manage the notifications

  Background: I am logged as an user
    Given I visit the main page in Web
    Then I login as an user

# Ver las notificaciones
@Notificac1
  Scenario: [NOTIFIC_01] I see alerts notifications
    Given I see the Home user page
    When I click on alerts notifications
    Then I see the notifications board
    # Implementar cuando se tenga usuario con notificaciones tipo alerta
    # Then I see the alerts in notification board

@Notificac2
  Scenario: [NOTIFIC_02] I see events notifications
    Given I see the Home user page
    When I click on events notifications
    Then I see the notifications board
    # Implementar cuando se tenga usuario con notificaciones tipo evento
    # Then I see the events in notification board

@Notificac3
  Scenario: [NOTIFIC_03] I see notices notifications
    Given I see the Home user page
    When I click on notices notifications
    Then I see the notifications board
    # Implementar cuando se tenga usuario con notificaciones tipo aviso
    #Then I see the events in notification board

@Notificac4
  Scenario: [NOTIFIC_04] I see all notifications
    Given I see the Home user page
    When I click on all notifications
    Then I see the notifications board
    # Implementar cuando se tenga usuario con notificaciones de cualquier tipo
    #Then I see the all notifications