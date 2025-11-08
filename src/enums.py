"""
This module implements all enumerations used in the application.

Author: Peyman Khodabandehlouei
Date: 07-11-2025
"""

from enum import Enum


class Gender(Enum):
    """Gender enumeration."""

    MALE = "male"
    FEMALE = "female"


class EmploymentType(Enum):
    """Employment type enumeration."""

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"


class VehicleStatus(Enum):
    """Employment type enumeration."""

    AVAILABLE = "available"
    RESERVED = "reserved"
    OUT_OF_SERVICE = "out_of_service"
