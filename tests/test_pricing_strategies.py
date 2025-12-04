"""
Test pricing strategies

This module contains unit tests for the pricing logic.
Here is a list of the available tests:
    1. First order pricing strategy which gives 15% discount on the first order.
    2. Loyalty pricing strategy which gives 10% discount on every 5th order.
    3. Normal pricing strategy which gives no discount on the first order.

Author: Peyman Khodabandehlouei
Date: 02-12-2025
"""


def test_first_order_pricing_strategy_calculations(
    get_customer,
    get_main_branch,
    get_compact_vehicle,
    get_gps_addon,
    get_premium_insurance_tier,
    get_pickup_and_return_dates,
):
    """Tests first order pricing logic with 15% discount on the first order."""
    # Get pickup and return dates
    pickup_date, return_date = get_pickup_and_return_dates

    # Create reservation
    reservation = get_customer.create_reservation(
        vehicle=get_compact_vehicle,
        insurance_tier=get_premium_insurance_tier,
        add_ons=[get_gps_addon],
        pickup_branch=get_main_branch,
        return_branch=get_main_branch,
        pickup_date=pickup_date,
        return_date=return_date,
    )

    # Manually calculate total price
    rental_days = (return_date - pickup_date).days

    vehicle_daily_rate = get_compact_vehicle.price_per_day
    insurance_daily_rate = get_premium_insurance_tier.price_per_day
    add_on_daily_rate = get_gps_addon.price_per_day

    # Calculate subtotal
    subtotal = (
        vehicle_daily_rate + insurance_daily_rate + add_on_daily_rate
    ) * rental_days

    # Apply 15% discount
    discount = subtotal * 0.15
    total_price = subtotal - discount

    assert rental_days == 3
    assert reservation.total_price == total_price


def test_loyalty_pricing_strategy_calculations(
    get_customer,
    get_main_branch,
    get_compact_vehicle,
    get_gps_addon,
    get_premium_insurance_tier,
    get_pickup_and_return_dates,
):
    """Tests loyalty pricing logic with 10% discount on every 5th order."""
    # Get pickup and return dates
    pickup_date, return_date = get_pickup_and_return_dates

    # Create 4 reservations and make the car available for another reservation
    for _ in range(4):
        # Reserve the car
        get_customer.create_reservation(
            vehicle=get_compact_vehicle,
            insurance_tier=get_premium_insurance_tier,
            add_ons=[get_gps_addon],
            pickup_branch=get_main_branch,
            return_branch=get_main_branch,
            pickup_date=pickup_date,
            return_date=return_date,
        )

        # Update the status
        get_compact_vehicle.make_available()

    # Reserve the car for 5th time
    get_customer.create_reservation(
        vehicle=get_compact_vehicle,
        insurance_tier=get_premium_insurance_tier,
        add_ons=[get_gps_addon],
        pickup_branch=get_main_branch,
        return_branch=get_main_branch,
        pickup_date=pickup_date,
        return_date=return_date,
    )

    # Manually calculate total price
    rental_days = (return_date - pickup_date).days

    vehicle_daily_rate = get_compact_vehicle.price_per_day
    insurance_daily_rate = get_premium_insurance_tier.price_per_day
    add_on_daily_rate = get_gps_addon.price_per_day

    # Calculate subtotal
    subtotal = (
        vehicle_daily_rate + insurance_daily_rate + add_on_daily_rate
    ) * rental_days

    # Apply 15% discount
    discount = subtotal * 0.10
    total_price = subtotal - discount

    # Access the last reservation
    last_reservation = get_customer.reservations[-1]

    assert last_reservation.total_price == total_price


def test_normal_pricing_strategy_calculations(
    get_customer,
    get_main_branch,
    get_compact_vehicle,
    get_economy_vehicle,
    get_gps_addon,
    get_premium_insurance_tier,
    get_pickup_and_return_dates,
):
    """Tests normal pricing logic with no discount on normal orders."""
    # Get pickup and return dates
    pickup_date, return_date = get_pickup_and_return_dates

    # Create reservation 1
    get_customer.create_reservation(
        vehicle=get_economy_vehicle,
        insurance_tier=get_premium_insurance_tier,
        add_ons=[get_gps_addon],
        pickup_branch=get_main_branch,
        return_branch=get_main_branch,
        pickup_date=pickup_date,
        return_date=return_date,
    )

    # Create reservation 2
    reservation = get_customer.create_reservation(
        vehicle=get_compact_vehicle,
        insurance_tier=get_premium_insurance_tier,
        add_ons=[get_gps_addon],
        pickup_branch=get_main_branch,
        return_branch=get_main_branch,
        pickup_date=pickup_date,
        return_date=return_date,
    )

    # Manually calculate total price
    rental_days = (return_date - pickup_date).days

    vehicle_daily_rate = get_compact_vehicle.price_per_day
    insurance_daily_rate = get_premium_insurance_tier.price_per_day
    add_on_daily_rate = get_gps_addon.price_per_day

    # Calculate subtotal
    total_price = (
        vehicle_daily_rate + insurance_daily_rate + add_on_daily_rate
    ) * rental_days

    assert reservation.total_price == total_price
