# Tests
This folder contains automated unittests for CRFMS system. The tests are designed for core business rules, workflows, and edge cases.

## Test Modules
1. **test_pricing_strategies.py**: This module tests different pricing strategies. The system has three pricing strategies: 
      - First Order Discount: `15% discount` on first order.
      - Loyalty Customer Discount: `10% discount` on every 5th order.
      - Normal pricing: No discount.

2. **test_reservations.py**: This module tests reservation logic. It tests different scenarios like:
      - Customer tries to reserve an `available` car.
      - Customer tries to reserve a vehicle that is already `reserved` and gets an error.
      - Customer tries to reserve a `picked-up` vehicle and gets an error.
      - Customer cancels a reservation with `pending` status successfully.
      - Customer cancels a reservation with `approved` status successfully.
      - Customer cancels a reservation with `picked_up` status and gets an error.
      - Customer cancels a reservation with `completed` status and gets an error.

3. **test_rental_flow**: This module tests full lifecycle of rental flow, including reservation, approval, payments, pickup, and return. Here is the full description of this specific unittest:
   1. Customer successfully creates a reservation for a vehicle.
   2. Customer attempts to pick up the vehicle but gets an error because an agent needs to approve the reservation first.
   3. Agent approves the reservation successfully.
   4. Customer attempts to pick up the vehicle again, but again faces an error because they need to complete the payment first.
   5. Customer completes the payment successfully using credit card.
   6. Customer picks up the vehicle successfully.
   7. Customer returns the vehicle successfully.
    


## How to run tests
1. Navigate to the tests folder using ```cd tests``` command from the root directory`.
2. Run the command: ```pytest -v```

## Changes during testing
1. Add AbstractClock to src for unittest.
2. Add custom errors to most entities for different scenarios during unittests.
3. Pricing Strategies used to only consider completed reservation for discount calculation, but this was a wrong approach, and has been fixed.
4. Notifications used to print a message on the console, but for unittest they are edited to return a string message.
5. Vehicle with status != 'available' were reservable, but this was a wrong business logic, and has been fixed. Now when a user wants to reserve an unavailable car, they will get `CarAlreadyReservedError`. 