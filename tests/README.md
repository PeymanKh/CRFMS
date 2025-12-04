# Tests
This folder contains automated unittests for CRFMS system. The tests are designed for core business rules, workflows, and edge cases.

## Test Modules
1. **test_pricing_strategies.py**: This module tests different pricing strategies. The system has three pricing strategies: 
      - First Order Discount: 15% discount on first order
      - Loyalty Customer Discount: 10% discount on every 5th order
      - Normal pricing: No discount

2. **test_reservations.py**: This module tests reservation logic. It tests different scenarios like:
      - Customer tries to reserve an available car
      - Customer tries to reserve a vehicle that is already reserved
      - Customer tries to reserve a picked-up vehicle

3. **test_rental_flow**:

## How to run tests
1. Navigate to the tests folder using ```cd tests``` command from the root directory`.
2. Run the command: ```pytest -v```

## Changes during testing
1. Pricing Strategies used to only consider completed reservation for discount calculation, but this was a wrong approach, and has been fixed.
2. Notifications used to print a message on the console, but for unittest they are edited to return a string message.
3. Vehicle with status != 'available' were reservable, but this was a wrong business logic, and has been fixed. Now when a user wants to reserve an unavailable car, they will get `CarAlreadyReservedError`. 