Feature: [DESNUBE] I revise the Desde La Nube page

Background: Start
    Given I visit the main page in web
    And I click register to web
    And I accept cookies
    And I click header servicios

@DesdeLaNube
  Scenario:[NUBE_01] Desde La Nube
    When I click to desde la nube
    Then I see page desde la nube
    And I request call