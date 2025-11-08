"""
This module implements VehicleClass class.
It is a concrete class and can directly initialize in the app.

Author: Peyman Khodabandehlouei
Date: 07-11-2025
"""

from datetime import date
from typing import Any, TYPE_CHECKING

from src.users.employee import Employee
from src.enums import Gender, EmploymentType


if TYPE_CHECKING:
    from src.branch.branch import Branch


class Manager(Employee):
    """
    Concrete class representing a Manager in the application.

    Args:
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
        branch: "Branch",
        is_active: bool,
        salary: float,
        hire_date: date,
        employment_type: EmploymentType,
    ) -> None:
        """Constructor method for Employee class."""
        # Call parent class constructor
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birth_date=birth_date,
            email=email,
            address=address,
            phone_number=phone_number,
            branch=branch,
            is_active=is_active,
            salary=salary,
            hire_date=hire_date,
            employment_type=employment_type,
        )

    def register_new_vehicle(self):
        """Adds new vehicle to the branch vehicles"""
        ...

    def remove_vehicle(self):
        """Removes a vehicle from branch vehicles"""
        ...

    def get_vehicle_information(self):
        """Returns information of a vehicle"""
        ...

    def approve_maintenance(self):
        """Approves the maintenance request created by an agent"""
        ...

    def get_role(self) -> str:
        """Returns role of the user in the application"""
        return "manager"

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
            "branch": self.branch.id,
            "is_active": self.is_active,
            "salary": self.salary,
            "hire_date": self.hire_date,
            "employment_type": self.employment_type,
        }

    def get_work_schedule(self) -> dict[str, str]:
        """
        Return work schedule details including hours and shift patterns.
        Schedules differ by employment type and role.
        """
        if self.employment_type == EmploymentType.FULL_TIME:
            return {
                "hours_per_week": "40",
                "monday": "09:00-17:00",
                "tuesday": "09:00-17:00",
                "wednesday": "09:00-17:00",
                "thursday": "09:00-17:00",
                "friday": "09:00-17:00",
                "saturday": "off",
                "sunday": "off",
            }
        elif self.employment_type == EmploymentType.PART_TIME:
            return {
                "hours_per_week": "20",
                "monday": "09:00-13:00",
                "tuesday": "off",
                "wednesday": "09:00-13:00",
                "thursday": "off",
                "friday": "09:00-13:00",
                "saturday": "10:00-15:00",
                "sunday": "off",
            }
        else:
            return {
                "hours_per_week": "40",
                "monday": "10:00-18:00",
                "tuesday": "10:00-18:00",
                "wednesday": "10:00-18:00",
                "thursday": "10:00-18:00",
                "friday": "10:00-18:00",
                "saturday": "off",
                "sunday": "off",
            }
