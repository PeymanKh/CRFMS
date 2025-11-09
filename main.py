from datetime import date

from src.enums import Gender, VehicleStatus
from src.users.agent import Agent
from src.branch.branch import Branch
from src.users.manager import Manager
from src.users.customer import Customer

from src.vehicle.vehicle import Vehicle
from src.reservation.add_on import AddOn
from src.vehicle.vehicle_class import VehicleClass
from src.reservation.insurance_tier import InsuranceTier

from src.reservation.reservation import Reservation


from src.enums import EmploymentType

if __name__ == "__main__":
    print("-"*20, "Create Branch, Customer, Agent, & Manager", "-"*20,)
    # Create a branch
    branch1 = Branch(
        name="Main branch",
        city="Istanbul",
        address="Nişantaşi, Istanbul",
        phone_number="+905343940796",
        employees=[],
    )
    print("New branch:", branch1)

    # Create a customer
    customer1 = Customer(
        first_name="Peyman",
        last_name="Khodabandehlouei",
        email="itspeey@gmail.com",
        phone_number="+905343940796",
        address="kağithane, Çeliktepe mah",
        gender=Gender.MALE,
        birth_date=date(1999, 6, 24),
    )
    print("New customer:", customer1)

    # Crate an agent
    agent1 = Agent(
        first_name="Derya",
        last_name="Yilmaz",
        email="ali@rental.com",
        phone_number="+905328973564",
        address="Beşiktaş",
        gender=Gender.FEMALE,
        birth_date=date(1989, 12,4),
        branch=branch1,
        is_active=True,
        salary=22_000,
        hire_date=date.today(),
        employment_type=EmploymentType.FULL_TIME,
    )
    print("New agent:", agent1)

    # Create a manager
    manager1 = Manager(
        first_name="Ömer",
        last_name="Erdamar",
        email="omer@rental.com",
        phone_number="+905323455",
        address="Beşiktaş",
        gender=Gender.MALE,
        birth_date=date(1992, 7, 12),
        branch=branch1,
        is_active=True,
        salary=40_000,
        hire_date=date.today(),
        employment_type=EmploymentType.FULL_TIME,
    )
    print("New manager:", manager1)

    # Check branch employees
    print("branch.employees():", branch1.employees, "\n")

    print("-" * 20, "Create Vehicle, AddOn, & InsuranceTier", "-" * 20)
    # Create a VehicleClass
    economy_class = VehicleClass(
        name="Economy",
        description="Compact and fuel-efficient vehicles ideal for city driving",
        base_daily_rate=35.00,
        features=["Air Conditioning", "4 Seats", "Bluetooth Audio"]
    )

    print("Economy vehicle class:", economy_class)

    # Create vehicle
    bmw = Vehicle(
        vehicle_class=economy_class,
        current_branch=branch1,
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
    print("BMW:", bmw)

    # Create AddOn
    gps_addon = AddOn(
        name="GPS",
        description="Premium GPS device with real-time traffic updates and offline maps",
        price_per_day=10.00
    )
    print("GPS AddOn:", gps_addon)

    child_sit_addon = AddOn(
        name="Child Safety Seat",
        description="Car seat for children aged 1-4 years, meets safety standards",
        price_per_day=5.00
    )
    print("Child safety seat AddOn:", child_sit_addon)

    insurance_tier = InsuranceTier(
        tier_name="Premium",
        description="Covers all damage, theft, and third-party liability up to $1,000,000",
        price_per_day=30.00
    )
    print("Premium insurance tier:", insurance_tier, "\n")

    print("-" * 20, "Reserve the Vehicle", "-" * 20)
    reservation = customer1.create_reservation(
        vehicle=bmw,
        insurance_tier=insurance_tier,
        pickup_branch=branch1,
        return_branch=branch1,
        pickup_date=date.today(),
        return_date=date.today(),
        add_ons=[gps_addon, child_sit_addon]
    )
    print("Reservation request by customer:", reservation)

    # Approve reservation by agent
    agent1.approve_reservation(reservation)
    print("Reservation approved by agent:", reservation)

