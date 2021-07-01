# Created by rapid at 6/21/2021
Feature: # Verify address, email and logo are here

  Scenario: # Verify address, email and logo are here
    Given Loginpage
    Then Verify address 1 "640 Ellicott Street" is here
    And Verify address 2 "Buffalo, NY 14203" is here
    And Verify email "hello@heyquelle.com" is here
    Then Verify logo "Quelle is the place that connects specialty contract recruiters directly to companies." is here