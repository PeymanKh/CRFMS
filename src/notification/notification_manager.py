"""
This module contains the concrete implementation of the NotificationManager,
which can directly initialize and used in the app.

Author: Peyman Khodabandehlouei
Date: 09-11-2025
"""

from typing import List, TYPE_CHECKING
from src.notification.notification_manager_interface import NotificationManagerInterface


if TYPE_CHECKING:
    from src.notification.subscriber_interface import Subscriber


class ConcreteNotificationManager(NotificationManagerInterface):
    """Concrete Subject. It manages subscribers"""
    def __init__(self):
        self._subscribers: List["Subscriber"] = []

    def attach(self, subscriber: "Subscriber"):
        print("Notification Manager: Attached a subscriber.")
        self._subscribers.append(subscriber)

    def detach(self, subscriber: "Subscriber"):
        print("Notification Manager: Detached a subscriber.")
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self)
