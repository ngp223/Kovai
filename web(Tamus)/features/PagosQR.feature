Feature: [PAGOSQR] I revise the Header

Background: Start
    Given I visit the main page in web
    And I click register to Web
    And I accept cookies
    And I click header servicios

@Cafeterias
  Scenario: [QR_01] Pagos QR
    When I click to pagos qr
    Then I see page pagos qr
    And I request call