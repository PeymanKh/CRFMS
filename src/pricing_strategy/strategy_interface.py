"""
This module implements interface for application's pricing strategies.
This is the first component of the Strategy design pattern.

Author: Peyman Khodabandehlouei
Date: 08-11-2025
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    """The Strategy interface declares operations common to all supported versions of pricing strategies"""

    @abstractmethod
    def calculate_price(self, vehicle: 'Vehicle') -> float:
        ...