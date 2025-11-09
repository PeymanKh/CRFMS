"""
This module implements concrete agent and user subscribers, They will recieve notifications
based on specific events in the application.

Author: Peyman Khodabandehlouei
Date: 09-11-2025
"""
from src.notification.subscriber_interface import Subscriber
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.notification.notification_manager_interface import NotificationManagerInterface


class CustomerSubscriber(Subscriber):
    """Concrete Subscriber. It notifies students about new assignments"""
    def update(self, subject: "NotificationManagerInterface"):
        print("From notification manager: Notification sent to the customer")


class AgentSubscriber(Subscriber):
    """Concrete Subscriber. It notifies students about new assignments"""
    def update(self, subject: "NotificationManagerInterface"):
        print("From notification manager: Notification sent to the agent")
