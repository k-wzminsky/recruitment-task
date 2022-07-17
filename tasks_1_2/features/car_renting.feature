Feature: Renting a car

  Background:
    Given the user is on Search car page

  Scenario Outline: In the <country>, <city> are available <available_cars_amount> cars for renting

    When the user selects the "Dropdowns.COUNTRY" with "<country>" value
    And the user selects the "Dropdowns.CITY" with "<city>" value
    And the user fills the "Inputs.PICK_UP_DATE" date field with "current_date" value
    And the user fills the "Inputs.DROP_OFF_DATE" date field with "current_date" value
    And the user clicks on the "Buttons.SEARCH"
    Then the users sees the displayed list of "<available_cars_amount>" available cars

    # Typo "Germainy" noted in bugs
    Examples: Test case for <country>, <city>
      | country  | city    | available_cars_amount |
      | France   | Paris   | 21                    |
      | Germainy | Berlin  | 25                    |
      | Poland   | Cracow  | 30                    |
      | Poland   | Wroclaw | 24                    |

  Scenario Outline: The price is correct counted based on the amount of renting days
    When the user selects the "Dropdowns.COUNTRY" with "<country>" value
    And the user selects the "Dropdowns.CITY" with "<city>" value
    And the user fills the "Inputs.PICK_UP_DATE" date field with "current_date" value
    And the user fills the "Inputs.DROP_OFF_DATE" date field with "<days>" later than pick-off date
    And the user clicks on the "Buttons.SEARCH"
    Then the users sees the list of cars with correct calculated price for amount of "<days>" days

    Examples: Test case for <country>, <city>
      | country  | city   | days |
      | France   | Paris  | 3    |
      | Germainy | Berlin | 5    |

  # Gherkin below should be cut off to smaller parts using execute_steps()
  # but I left in this form for easier review
  Scenario Outline: The user verifies details and rents in <country>, <city> from the <company_name>, <model>, <plate_number> car
    When the user selects the "Dropdowns.COUNTRY" with "<country>" value
    And the user selects the "Dropdowns.CITY" with "<city>" value
    And the user fills the "Inputs.MODEL" field with "<model>" value
    And the user fills the "Inputs.PICK_UP_DATE" date field with "current_date" value
    And the user fills the "Inputs.DROP_OFF_DATE" date field with "current_date" value
    And the user clicks on the "Buttons.SEARCH"
    And the user gets the price per day for car with "<plate_number>" plate number
    And the user clicks on the Rent button for car with "<plate_number>" plate number
    Then the user is redirected to the "RentDetailsPage"

    And the correct "<company_name>" company name, rent details and dates are displayed
    But the user clicks on the "Buttons.RENT"
    Then the user is redirected to the "SummaryRentDetailsPage"

    And the correct "<company_name>" company summary details are displayed
    When the user fills the "Inputs.NAME" field with "John" value
    And the user fills the "Inputs.LAST_NAME" field with "Doe" value
    And the user fills the "Inputs.CARD_NUMBER" field with "123456" value
    And the user fills the "Inputs.EMAIL" field with "example@email.com" value
    Then there are no inputs error messages displayed

    Examples:
      | country  | city    | model             | company_name | plate_number |
      | Germainy | Berlin  | Volkswagen Touran | Adams Group  | 384 OIC      |
      | Poland   | Wroclaw | Skoda Octavia     | Kirk-Norton  | 0-E4643      |
