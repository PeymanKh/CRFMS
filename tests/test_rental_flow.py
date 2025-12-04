"""
Test rental flow module

This module contains unit tests for the rental flow. The main goal of this module is to test
the rental process which is as follows:
    1. A customer reserves an available vehicle.
    2. An agent approves the reservation if everything is ok.
"""
import pytest
from datetime import date, timedelta


def test_rental_flow_success(
        get_customer,
        get_main_branch,
        get_active_agent,
        get_economy_vehicle,
        get_gps_addon,
        get_premium_insurance_tier,
):
    # Create date objects for pickup and return dates (Total 3 days)
    pickup_date = date.today() + timedelta(days=1)
    return_date = pickup_date + timedelta(days=12)

    # Customer makes a reservation
    get_customer.create_reservation(
        vehicle=get_economy_vehicle,
        insurance_tier=get_premium_insurance_tier,
        add_ons=[get_gps_addon],
        pickup_branch=get_main_branch,
        return_branch=get_main_branch,
        pickup_date=pickup_date,
        return_date=return_date,
    )

    assert get_economy_vehicle.status == "reserved"


