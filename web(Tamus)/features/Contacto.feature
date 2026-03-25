Feature: [CONTACT] I revise the Contacto Page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies

@Contacto
  Scenario:[CONTACT_01] Contacto
    When I click to contacto
    Then I see page contacto
    And I request call contact
