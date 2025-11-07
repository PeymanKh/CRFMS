"""
This module implements concrete Branch class.
This class is a concrete class and can directly initialize in the app.

Note: Since Branch has employees attribute, inner class Employee import is used to avoid circular import issue.

Author: Peyman Khodabandehlouei
Date: 30-10-2025
"""

import uuid
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.users.employee import Employee


class Branch:
    """
    Concrete class representing a branch in the application.
    This class can be directly initialized and used during application runtime.

    Args:
        name (str): Name of the branch.
        city (str): City of the branch.
        address (str): Address of the branch.
        phone_number (str): Phone number of the branch.
        employees (Optional[List[Employee]]): List of employees working in the branch.
            Defaults to an empty list if not provided.
    """

    def __init__(
        self,
        name: str,
        city: str,
        address: str,
        phone_number: str,
        employees: Optional[List["Employee"]] = None,
    ) -> None:
        """Constructor method for Branch class."""
        # Validate name
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if name == "":
            raise ValueError("Name cannot be empty.")

        # Validate city
        if not isinstance(city, str):
            raise TypeError("City must be a string.")
        if city == "":
            raise ValueError("City cannot be empty.")

        # Validate address
        if not isinstance(address, str):
            raise TypeError("Address must be a string.")
        if address == "":
            raise ValueError("Address cannot be empty.")

        # Validate phone_number
        if not isinstance(phone_number, str):
            raise TypeError("Phone number must be a string.")
        if phone_number == "":
            raise ValueError("Phone number cannot be empty.")

        # Validate employees
        if employees is None:
            employees = []
        else:
            # Validate employee is a list
            if not isinstance(employees, list):
                raise ValueError("employees must be a list.")
            # Validate all items in the list are Employee instances
            from src.users.employee import Employee  # To avoid circular import

            if not all(isinstance(employee, Employee) for employee in employees):
                raise ValueError("All employees must be instances of Employee class.")

        # Assign values
        self.__id = str(uuid.uuid4())
        self.__name = name
        self.__city = city
        self.__address = address
        self.__phone_number = phone_number
        self.__employees = employees

    @property
    def id(self) -> str:
        """
        Getter method for id property.

        Note: ID is auto-generated and immutable. Cannot be modified after creation.
        """
        return self.__id

    @property
    def name(self) -> str:
        """Getter method for name property."""
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        """Setter method for name property."""
        # Validation
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        if new_name == "":
            raise ValueError("Name cannot be empty.")

        # Business logic
        self.__name = new_name

    @property
    def city(self) -> str:
        """Getter method for city property."""
        return self.__city

    @city.setter
    def city(self, new_city) -> None:
        """Setter method for city property."""
        # Validation
        if not isinstance(new_city, str):
            raise TypeError("City must be a string.")
        if new_city == "":
            raise ValueError("City cannot be empty.")

        # Business logic
        self.__city = new_city

    @property
    def address(self) -> str:
        """Getter method for address property."""
        return self.__address

    @address.setter
    def address(self, new_address) -> None:
        """Setter method for address property"""
        # Validation
        if not isinstance(new_address, str):
            raise TypeError("Address must be a string.")
        if new_address == "":
            raise ValueError("Address cannot be empty.")

        # Business logic
        self.__address = new_address

    @property
    def phone_number(self) -> str:
        """Getter method for phone_number property."""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number) -> None:
        """Setter method for phone_number property."""
        # Validation
        if not isinstance(new_phone_number, str):
            raise TypeError("Phone number must be a string.")
        if new_phone_number == "":
            raise ValueError("Phone number cannot be empty.")

        # Business logic
        self.__phone_number = new_phone_number

    @property
    def employees(self) -> List["Employee"]:
        """Getter method for employees"""
        return self.__employees

    @employees.setter
    def employees(self, new_employees: List["Employee"]) -> None:
        """
        Setter method for employees property.

        Args:
            new_employees (List[Employee]): A list of Employee instances.

        Raises:
            ValueError: If new_employees is not a list.
            TypeError: If any item is not an Employee instance.
        """
        # Validation
        if not isinstance(new_employees, list):
            raise ValueError("Employees must be a list.")

        if len(new_employees) == 0:
            raise ValueError("Employees list cannot be empty.")

        from src.users.employee import Employee  # To avoid circular import

        if not all(isinstance(emp, Employee) for emp in new_employees):
            raise TypeError("All employees must be instances of Employee class.")

        # Business logic
        self.__employees = new_employees

    def has_employee(self, employee_id: str) -> bool:
        """
        Method to check if an employee is working in the branch.

        Args:
            employee_id (str): The unique ID of the employee to search for.

        Returns:
            bool: True if an employee matching the criteria is found, False otherwise.

        Raises:
            ValueError: If no search criteria are provided.
        """
        if not employee_id:
            raise ValueError("Employee ID is required.")

        return any(emp.id == employee_id for emp in self.__employees)

    def add_employee(self, employee: "Employee") -> None:
        """
        Method to add a new employee to the branch.

        Args:
            employee (Employee): The employee to add.

        Raises:
            ValueError: If the employee is already in the branch.
        """
        # Validate employee is an instance of Employee class
        from src.users.employee import Employee  # To avoid circular import

        if not isinstance(employee, Employee):
            raise ValueError("Employee must be an instance of Employee class.")

        # Validate if employee is not already working in the branch
        if any(emp.id == employee.id for emp in self.__employees):
            raise ValueError("Employee is already working in the branch.")

        self.__employees.append(employee)

    def remove_employee(self, employee_id: str) -> None:
        """
        Method to remove an employee from the branch.

        Args:
            employee_id (str): The unique ID of the employee to remove.

        Raises:
            ValueError: If no employee with the given ID is found.
        """
        # Validate employee_id is a string
        if not isinstance(employee_id, str):
            raise ValueError("Employee ID must be a string.")

        # Check if employee exists in the branch
        if not self.has_employee(employee_id):
            raise ValueError("Employee with the given ID is not found.")

        self.__employees = [emp for emp in self.__employees if emp.id != employee_id]
