"""
Fixed instances for testing

This module implements instances that can be used in all test functions.
They are implemented using @pytest.fixture decorator.

Author: Peyman Khodabandehlouei
Date: 01-12-2025
"""

import pytest
from datetime import date

from src.enums import Gender, EmploymentType, VehicleStatus
from src.branch.branch import Branch
from src.users.agent import Agent
from src.users.manager import Manager
from src.users.customer import Customer
from src.vehicle.vehicle_class import VehicleClass
from src.vehicle.vehicle import Vehicle


@pytest.fixture
def get_main_branch() -> Branch:
    """
    Returns a Branch instance with the following properties:
        1. Name: Main branch
        2. City: Istanbul
        3. Address: Kaġithane merkez
        4. Phone number: +905343940796
    """
    return Branch(
        name="Main branch",
        city="Istanbul",
        address="Kaġithane merkez",
        phone_number="+905343940796",
    )


@pytest.fixture
def get_customer() -> Customer:
    """
    Returns a Customer instance with the following properties:
        1. First name: Peyman
        2. Last name: Khodabandehlouei
        3. Gender: Male
        4. Birthdate: 1995-01-01
        5. Email: itspeey@gmail.com
        6. Address: Beşiktaş
        7. Phone number: +905343940796
    """
    return Customer(
        first_name="Peyman",
        last_name="Khodabandehlouei",
        gender=Gender.MALE,
        birth_date=date(1995, 1, 1),
        email="itspeey@gmai.com",
        address="Beşiktaş",
        phone_number="+905343940796",
    )


@pytest.fixture
def get_active_agent(get_main_branch) -> Agent:
    """
    Returns an Agent instance with the following properties:
        1. First name: Buse
        2. Last name: Yilmaz
        3. Gender: Female
        4. Birthdate: 1990-01-01
        5. Email: buse.yilmaz@business.com
        6. Address: Kadiköy
        7. Phone number: +905343940796
        8. Branch: Branch("Main branch")
        9. Is active: True
        10. Salary: 20_000
        11. Hire date: 2015-01-01
        12. Employment type: Full time
    """
    return Agent(
        first_name="Buse",
        last_name="Yilmaz",
        gender=Gender.FEMALE,
        birth_date=date(1990, 1, 1),
        email="buse.yilmaz@business.com",
        address="Kadiköy",
        phone_number="905343940796",
        branch=get_main_branch,
        is_active=True,
        salary=20_000,
        hire_date=date(2015, 1, 1),
        employment_type=EmploymentType.FULL_TIME,
    )


@pytest.fixture
def get_active_manager(get_main_branch) -> Manager:
    """
    Returns a Manager instance with the following properties:
        1. First name: Ali
        2. Last name: Talha
        3. Gender: Male
        4. Birthdate: 1985-01-01
        5. Email: ali.talha@business.com
        6. Address: Kadiköy
        7. Phone number: +905343940796
        8. Branch: Branch("Main branch")
        9. Is active: True
        10. Salary: 40_000
        11. Hire date: 2010-01-01
        12. Employment type: Full time
    """
    return Manager(
        first_name="Ali",
        last_name="Talha",
        gender=Gender.MALE,
        birth_date=date(1985, 1, 1),
        email="ali.talha@business.com",
        address="Kadiköy",
        phone_number="905343940796",
        branch=get_main_branch,
        is_active=True,
        salary=40_000,
        hire_date=date(2010, 1, 1),
        employment_type=EmploymentType.FULL_TIME,
    )


@pytest.fixture
def get_economy_vehicle_class() -> VehicleClass:
    """
    Returns a VehicleClass instance with the following properties:
        1. Name: Economy
        2. Description: Small, fuel-efficient vehicles for city driving.
        3. Base daily rate: 30.0
        4. Features: ["Air conditioning", "Manual transmission"]
    """
    return VehicleClass(
        name="Economy",
        description="Small, fuel-efficient vehicles for city driving.",
        base_daily_rate=30.0,
        features=[
            "Air conditioning",
            "Manual transmission",
        ],
    )


@pytest.fixture
def get_compact_vehicle_class() -> VehicleClass:
    """
    Returns a VehicleClass instance with the following properties:
        1. Name: Compact
        2. Description: Compact cars with more space and comfort than economy class.
        3. Base daily rate: 45.0
        4. Features: ["Air conditioning", "Automatic transmission"]
    """
    return VehicleClass(
        name="Compact",
        description="Compact cars with more space and comfort than economy class.",
        base_daily_rate=45.0,
        features=[
            "Air conditioning",
            "Automatic transmission",
        ],
    )


@pytest.fixture
def get_suv_vehicle_class() -> VehicleClass:
    """
    Returns a VehicleClass instance with the following properties:
        1. Name: SUV
        2. Description: Larger vehicles suitable for families and long trips.
        3. Base daily rate: 70.0
        4. Features: ["Automatic transmission", "All-wheel drive"]
    """
    return VehicleClass(
        name="SUV",
        description="Larger vehicles suitable for families and long trips.",
        base_daily_rate=70.0,
        features=[
            "Automatic transmission",
            "All-wheel drive",
        ],
    )


@pytest.fixture
def get_economy_vehicle(get_economy_vehicle_class, get_main_branch) -> Vehicle:
    """
    Returns an Economy class Vehicle instance (Toyota Yaris) with the following properties:
        1. Vehicle class: Economy
        2. Current branch: Main branch
        3. Status: AVAILABLE
        4. Brand: Toyota
        5. Model: Yaris
        6. Color: White
        7. Licence plate: ECN-001
        8. Fuel level: 0.8
        9. Last service odometer: 10_000
        10. Odometer: 12_500
        11. Price per day: get_economy_vehicle_class.base_daily_rate + 5
        12. Maintenance records: []
    """
    return Vehicle(
        vehicle_class=get_economy_vehicle_class,
        current_branch=get_main_branch,
        status=VehicleStatus.AVAILABLE,
        brand="Toyota",
        model="Yaris",
        color="White",
        licence_plate="ECN-001",
        fuel_level=0.8,
        last_service_odometer=10_000,
        odometer=12_500,
        price_per_day=get_economy_vehicle_class.base_daily_rate + 5,
        maintenance_records=[],
    )


@pytest.fixture
def get_compact_vehicle(get_compact_vehicle_class, get_main_branch) -> Vehicle:
    """
    Returns a Compact class Vehicle instance (Volkswagen Golf) with the following properties:
        1. Vehicle class: Compact
        2. Current branch: Main branch
        3. Status: AVAILABLE
        4. Brand: Volkswagen
        5. Model: Golf
        6. Color: Gray
        7. Licence plate: CMP-001
        8. Fuel level: 0.7
        9. Last service odometer: 20_000
        10. Odometer: 22_000
        11. Price per day: get_compact_vehicle_class.base_daily_rate + 10
        12. Maintenance records: []
    """
    return Vehicle(
        vehicle_class=get_compact_vehicle_class,
        current_branch=get_main_branch,
        status=VehicleStatus.AVAILABLE,
        brand="Volkswagen",
        model="Golf",
        color="Gray",
        licence_plate="CMP-001",
        fuel_level=0.7,
        last_service_odometer=20_000,
        odometer=22_000,
        price_per_day=get_compact_vehicle_class.base_daily_rate + 10,
        maintenance_records=[],
    )


@pytest.fixture
def get_suv_vehicle(get_suv_vehicle_class, get_main_branch) -> Vehicle:
    """
    Returns an SUV class Vehicle instance (Toyota RAV4) with the following properties:
        1. Vehicle class: SUV
        2. Current branch: Main branch
        3. Status: AVAILABLE
        4. Brand: Toyota
        5. Model: RAV4
        6. Color: Black
        7. Licence plate: SUV-001
        8. Fuel level: 0.9
        9. Last service odometer: 30_000
        10. Odometer: 33_000
        11. Price per day: get_suv_vehicle_class.base_daily_rate + 20
        12. Maintenance records: []
    """
    return Vehicle(
        vehicle_class=get_suv_vehicle_class,
        current_branch=get_main_branch,
        status=VehicleStatus.AVAILABLE,
        brand="Toyota",
        model="RAV4",
        color="Black",
        licence_plate="SUV-001",
        fuel_level=0.9,
        last_service_odometer=30_000,
        odometer=33_000,
        price_per_day=get_suv_vehicle_class.base_daily_rate + 20,
        maintenance_records=[],
    )
