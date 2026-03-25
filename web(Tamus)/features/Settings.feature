# Created by mshi0 at 23/02/2024
@TamusWeb
Feature: [SETTING] I put seetings for a user

  Background: I am logged as an user
    Given I visit the main page in Web
    Then I login as an user

# Activar opciones
@Settings @SettingsOn1
  Scenario: [SETTING_01] I go into settings page
    Given I see the Home user page
    When I click on settings
    Then I see the settings page

@SettingOn @SettingsOn2
  Scenario: [SETTING_02] I active the option incoming delivery pending
    Given I click on settings
    When I activate the option incoming delivery pending
    Then I see the option incoming delivery pending actived

@SettingsOn @SettingsOn3
  Scenario: [SETTING_03] I active the option departure delivery pending
    Given I click on settings
    When I activate the option departure delivery pending
    Then I see the option departure delivery pending actived

@SettingsOn @SettingsOn4
  Scenario: [SETTING_04] I active the option incoming delivery rejected
    Given I click on settings
    When I activate the option incoming delivery rejected
    Then I see the option incoming delivery rejected actived

@SettingsOn @SettingsOn5
  Scenario: [SETTING_05] I active the option departure delivery rejected
    Given I click on settings
    When I activate the option departure delivery rejected
    Then I see the option departure delivery rejected actived

@SettingsOn @SettingsOn6
  Scenario: [SETTING_06] I active the option low stock
    Given I click on settings
    When I activate the option low stock
    Then I see the option low stock actived

# Desactivar opciones
@SettingsOff @SettingsOff7
  Scenario: [SETTING_07] I deactivate the option incoming delivery pending
    Given I click on settings
    When I deactivate the option incoming delivery pending
    Then I see the option incoming delivery pending deactivated

@SettingsOff @SettingsOff8
  Scenario: [SETTING_08] I deactivate the option departure delivery pending
    Given I click on settings
    When I deactivate the option departure delivery pending
    Then I see the option departure delivery pending deactivated

@SettingsOff @SettingsOff9
  Scenario: [SETTING_09] I deactivate the option incoming delivery rejected
    Given I click on settings
    When I deactivate the option incoming delivery rejected
    Then I see the option incoming delivery rejected deactivated

@SettingsOff @SettingsOff10
  Scenario: [SETTING_10] I deactivate the option departure delivery rejected
    Given I click on settings
    When I deactivate the option departure delivery rejected
    Then I see the option departure delivery rejected deactivated

@SettingsOff @SettingsOff11
  Scenario: [SETTING_11] I deactivate the option low stock
    Given I click on settings
    When I deactivate the option low stock
    Then I see the option low stock deactivated