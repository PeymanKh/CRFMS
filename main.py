"""
This module tests the application, Note that to keep this module clean, I moved all creational
logic to utils.py.

Author: Peyman Khodabandehlouei
Date: 09-11-2025
"""

import utils
from datetime import date


if __name__ == "__main__":
    print("-"*20, "Create Branch, Customer, Agent, & Manager", "-"*20,)

    # Create a branch
    branch = utils.create_test_branch()
    print("New branch:", branch)

    # Create a customer
    customer = utils.create_test_customer()
    print("New customer:", customer)

    # Crate an agent
    agent = utils.create_test_agent(branch=branch)
    print("New agent:", agent)

    # Create a manager
    manager = utils.create_test_manager(branch=branch)
    print("New manager:", manager)

    # Check branch employees
    print("branch.employees():", branch.employees, "\n")

    print("-" * 20, "Create Vehicle, AddOn, & InsuranceTier", "-" * 20)

    # Create a VehicleClass
    economy_class = utils.create_economy_vehicle_class()
    print("Economy vehicle class:", economy_class)

    # Create vehicle
    bmw = utils.create_bmw(economy_class, branch)
    print("BMW:", bmw)

    # Create AddOns
    gps_addon = utils.create_gps_addon()
    print("GPS AddOn:", gps_addon)
    child_sit_addon = utils.create_child_seat_addon()
    print("Child safety seat AddOn:", child_sit_addon)

    # Create InsuranceTier
    insurance_tier = utils.create_premium_insurance_tier()
    print("Premium insurance tier:", insurance_tier, "\n")

    print("-" * 20, "Create NotificationManager and Subscribe Customer & Agent", "-" * 20)
    notification_manager = utils.create_notification_manager()
    print("")

    print("-" * 20, "Reserve the Vehicle", "-" * 20)

    # Create a reservation by the user
    reservation = customer.create_reservation(
        vehicle=bmw,
        insurance_tier=insurance_tier,
        pickup_branch=branch,
        return_branch=branch,
        pickup_date=date.today(),
        return_date=date.today(),
        add_ons=[gps_addon, child_sit_addon]
    )
    print("Reservation request by customer:", reservation)

    # Send notification to the customer and agent
    notification_manager.notify()

    # Approve the reservation
    agent.approve_reservation(reservation)
    print("Reservation approved by agent:", reservation, "\n")

    print("-" * 20, "Make Payment", "-" * 20)

    # Make payment
    receipt = customer.make_creditcard_payment(reservation, "1234 1234 1234 1234", "123", "12/30")
    print("Payment receipt:", receipt)

    if "successful" in receipt:
        reservation.invoice.payment_completed()

    else:
        reservation.invoice.payment_failed()

    # Print invoice
    print("Invoice:", reservation.invoice)
