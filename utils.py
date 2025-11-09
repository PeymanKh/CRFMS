"""
This module implements utility functions to create entities so the main.py remains clean

Author: Peyman Khodabandehlouei
Date: 09-11-2025
"""
from datetime import date

from src.enums import Gender, VehicleStatus, EmploymentType
from src.users.agent import Agent
from src.branch.branch import Branch
from src.users.manager import Manager
from src.users.customer import Customer

from src.vehicle.vehicle import Vehicle
from src.reservation.add_on import AddOn
from src.vehicle.vehicle_class import VehicleClass
from src.reservation.insurance_tier import InsuranceTier


def create_test_branch():
    """Creates a test branch"""
    branch = Branch(
        name="Main branch",
        city="Istanbul",
        address="Nişantaşi, Istanbul",
        phone_number="+905343940796",
        employees=[],
    )
    return branch


def create_test_customer():
    """Creates a test customer"""

    customer = Customer(
        first_name="Peyman",
        last_name="Khodabandehlouei",
        email="itspeey@gmail.com",
        phone_number="+905343940796",
        address="kağithane, Çeliktepe mah",
        gender=Gender.MALE,
        birth_date=date(1999, 6, 24),
    )

    return customer


def create_test_agent(branch):
    """Creates a test agent"""
    agent = Agent(
        first_name="Derya",
        last_name="Yilmaz",
        email="ali@rental.com",
        phone_number="+905328973564",
        address="Beşiktaş",
        gender=Gender.FEMALE,
        birth_date=date(1989, 12,4),
        branch=branch,
        is_active=True,
        salary=22_000,
        hire_date=date.today(),
        employment_type=EmploymentType.FULL_TIME,
    )

    return agent

def create_test_manager(branch):
    """Creates a test manager"""
    manager = Manager(
        first_name="Ömer",
        last_name="Erdamar",
        email="omer@rental.com",
        phone_number="+905323455",
        address="Beşiktaş",
        gender=Gender.MALE,
        birth_date=date(1992, 7, 12),
        branch=branch,
        is_active=True,
        salary=40_000,
        hire_date=date.today(),
        employment_type=EmploymentType.FULL_TIME,
    )
    return manager

def create_economy_vehicle_class():
    """Creates a test vehicle class"""
    economy_class = VehicleClass(
        name="Economy",
        description="Compact and fuel-efficient vehicles ideal for city driving",
        base_daily_rate=35.00,
        features=["Air Conditioning", "4 Seats", "Bluetooth Audio"]
    )

    return economy_class


def create_bmw(vehicle_class, branch):
    """Creates a test vehicle"""
    bmw = Vehicle(
        vehicle_class=vehicle_class,
        current_branch=branch,
        status=VehicleStatus.AVAILABLE,
        brand="BMW",
        model="230i",
        color="Sky Blue",
        licence_plate="12 MBA 342",
        fuel_level=100.0,
        last_service_odometer=45000.0,
        odometer=48500.0,
        price_per_day=45.00
    )

    return bmw

def create_gps_addon():
    """Creates a GPS AddOn"""
    gps_addon = AddOn(
        name="GPS",
        description="GPS device for vehicle navigation",
        price_per_day=10.00
    )

    return gps_addon

def create_child_seat_addon():
    """Creates a child seat AddOn"""
    child_seat_addon = AddOn(
        name="Child Safety Seat",
        description="Child safety seat for children aged 1-4 years",
        price_per_day=5.00
    )

    return child_seat_addon

def create_premium_insurance_tier():
    """Creates a premium insurance tier"""
    premium_insurance_tier = InsuranceTier(
        tier_name="Premium",
        description="Covers all damage, theft, and third-party liability up to $1,000,000",
        price_per_day=30.00
    )

    return premium_insurance_tier
