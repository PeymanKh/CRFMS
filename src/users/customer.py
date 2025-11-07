"""
This module implements Customer class.
It is a concrete class and can directly initialize in the app.

Author: Peyman Khodabandehlouei
Date: 30-10-2025
"""

from datetime import date
from typing import Any, Optional, List, TYPE_CHECKING

from src.enums import Gender
from src.users.base_user import BaseUser


if TYPE_CHECKING:
    from src.branch.branch import Branch


class Customer(BaseUser):
    """
    Concrete class representing a customer in the application.

    Args:
        first_name (str): First name of the employee.
        last_name (str): Last name of the employee.
        gender (Gender): Gender of the employee (Gender enum).
        birth_date (date): Birth date of the employee (must be >= 18 years ago).
        email (EmailStr): Email address of the employee.
        address (str): Home address of the employee.
        phone_number (str): Phone number of the employee.
        reservations (Reservation): Reservations made by the customer.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: Gender,
        birth_date: date,
        email: str,
        address: str,
        phone_number: str,
        reservations: Optional[List["Reservation"]] = None,
    ) -> None:
        """Constructor method for BaseUser class."""
        # Call parent class constructor
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birth_date=birth_date,
            email=email,
            address=address,
            phone_number=phone_number,
        )

        # Validate reservation
        if reservations is None:
            reservations = []
        else:
            # Validate employee is a list
            if not isinstance(reservations, list):
                raise ValueError("reservations must be a list.")
            # Validate all items in the list are Employee instances
            from src.users.employee import Employee  # To avoid circular import

            if not all(
                isinstance(reservation, Employee) for reservation in reservations
            ):
                raise ValueError("All employees must be instances of Employee class.")

        # Assign reservations
        self.__reservations = reservations

    @property
    def reservations(self):
        """Getter method for reservations."""
        return self.__reservations

    def get_reservations(self):
        """Returns all reservations created by the customer"""
        return self.__reservations

    def create_reservation(self):
        """Creates a new reservation and adds it to the customer reservations"""
        ...

    def cancel_reservation(self):
        """Cancel the reservation if it was created by the user."""
        ...

    def pickup_vehicle(self):
        """"""
        ...

    def return_vehicle(self):
        """"""
        ...

    def get_role(self) -> str:
        """Returns role of the user in the application"""
        return "customer"

    def get_information(self) -> dict[str, Any]:
        """Returns a dictionary including all user information"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "reservations": self.__reservations,
        }
