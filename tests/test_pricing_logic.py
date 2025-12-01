"""
This module contains unit tests for the pricing logic.
Here is a list of the available tests:

"""
from datetime import date, timedelta

from src.enums import ReservationStatus
from src.reservation.reservation import Reservation


def test_first_order_pricing(
    get_customer, get_main_branch, get_compact_vehicle, get_gps_addon, get_premium_insurance_tier
):
    """
    Tests first order pricing logic which gives 15% discount on the first order

    The flow of this test is as follows:
        1- User creates a reservation.
    """
    # Create date objects for pickup and return dates (Total 3 days)
    pickup_date = date.today() + timedelta(days=1)
    return_date = pickup_date + timedelta(days=3)

    reservation = Reservation(
        status=ReservationStatus.PENDING,
        creator=get_customer,
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
    subtotal = (vehicle_daily_rate + insurance_daily_rate + add_on_daily_rate) * rental_days

    # Apply 15% discount
    discount = subtotal * 0.15
    total_price = subtotal - discount

    assert reservation.total_price == total_price

