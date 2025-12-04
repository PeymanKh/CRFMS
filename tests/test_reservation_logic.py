"""
Test rental flow module

This module contains unit tests for the rental business logic.
Here is a list of the available tests:
    1. Reserve an Available vehicle.
    2. Reserve a RESERVED vehicle.
    3. Reserve a PICKED_UP vehicle.
    4. Reserve a car with return date before pickup date.

Author: Peyman Khodabandehlouei
Date: 02-12-2025
"""
import pytest
from datetime import date, timedelta

from src.enums import VehicleStatus, ReservationStatus
from src.custom_errors import ReturnDateBeforePickupDateError, VehicleNotAvailableError


def test_reserve_available_vehicle_success(
        get_customer,
        get_main_branch,
        get_compact_vehicle,
        get_gps_addon,
        get_premium_insurance_tier,
):
    """Test reservation of an available vehicle."""
    # Create date objects for pickup and return dates (Total 3 days)
    pickup_date = date.today() + timedelta(days=1)
    return_date = pickup_date + timedelta(days=3)

    # Create reservation
    get_customer.create_reservation(
        vehicle=get_compact_vehicle,
        insurance_tier=get_premium_insurance_tier,
        add_ons=[get_gps_addon],
        pickup_branch=get_main_branch,
        return_branch=get_main_branch,
        pickup_date=pickup_date,
        return_date=return_date,
    )

    assert len(get_customer.reservations) == 1
    assert get_customer.reservations[0].status == ReservationStatus.PENDING.value
    assert get_customer.reservations[0].vehicle.status == VehicleStatus.RESERVED.value


def test_reserve_reserved_vehicle_failure(
        get_customer,
        get_main_branch,
        get_compact_vehicle,
        get_gps_addon,
        get_premium_insurance_tier,
):
    """Test reservation of a reserved vehicle error."""
    # Create date objects for pickup and return dates (Total 3 days)
    pickup_date = date.today() + timedelta(days=1)
    return_date = pickup_date + timedelta(days=3)

    # Change vehicle status to reserved
    get_compact_vehicle.status = VehicleStatus.RESERVED

    # Create reservation
    with pytest.raises(VehicleNotAvailableError):
        get_customer.create_reservation(
            vehicle=get_compact_vehicle,
            insurance_tier=get_premium_insurance_tier,
            add_ons=[get_gps_addon],
            pickup_branch=get_main_branch,
            return_branch=get_main_branch,
            pickup_date=pickup_date,
            return_date=return_date,
        )


def test_reserve_picked_up_vehicle_failure(
        get_customer,
        get_main_branch,
        get_compact_vehicle,
        get_gps_addon,
        get_premium_insurance_tier,
):
    """Test reservation of a reserved vehicle error."""
    # Create date objects for pickup and return dates (Total 3 days)
    pickup_date = date.today() + timedelta(days=1)
    return_date = pickup_date + timedelta(days=3)

    # Change vehicle status to reserved
    get_compact_vehicle.status = VehicleStatus.PICKED_UP

    # Create reservation
    with pytest.raises(VehicleNotAvailableError):
        get_customer.create_reservation(
            vehicle=get_compact_vehicle,
            insurance_tier=get_premium_insurance_tier,
            add_ons=[get_gps_addon],
            pickup_branch=get_main_branch,
            return_branch=get_main_branch,
            pickup_date=pickup_date,
            return_date=return_date,
        )


def test_return_date_before_pickup_date_failure(
        get_customer,
        get_main_branch,
        get_compact_vehicle,
        get_gps_addon,
        get_premium_insurance_tier,

):
    """Test reservation of a vehicle with return date before pickup date error."""
    # Create date objects for pickup and return dates (Total 3 days)
    pickup_date = date.today() + timedelta(days=3)
    return_date = date.today() + timedelta(days=1)

    with pytest.raises(ReturnDateBeforePickupDateError):

        # Create reservation
        get_customer.create_reservation(
            vehicle=get_compact_vehicle,
            insurance_tier=get_premium_insurance_tier,
            add_ons=[get_gps_addon],
            pickup_branch=get_main_branch,
            return_branch=get_main_branch,
            pickup_date=pickup_date,
            return_date=return_date,
        )

