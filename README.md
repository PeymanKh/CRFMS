# Car Rental & Fleet Management System (CRFMS)

> This project is implementation of a Car Rental & Fleet Management System for advanced python course. I strongly suggest reading this README.md file to fully understand my approach and design system. 

## 1. Introduction
The main goal of this project is to create a CRFMS system with respect to SOLID principles and GoF design patterns. *Factory Method*, *Template Method*, *Observer*, and *Strategy* design patterns are used to solve specific architectural challenges. In this document I will explain all entities used in the project, the reason behind my design, and the business rules I have defined.

## 2. Design Philosophy
1. **Users:** User (person) is the first entity in the system. For designing users including customers and employees, I inspired by `LangChain API design`. It has a base class for everything then expands those base classes to create specific objects. For example, it has a `BaseMessage` class which is a blueprint of creating messages in the ecosystem and different kind of messages such as `AIMessage`, `UserMessage`, or `ToolMessage` are inherited from `BaseMessage`. So in my design I have defined a [BaseUser](src/users/base_user.py) class, which is a blueprint for all different kinds of users envolved in the application. Then, I created an [Employee](src/users/employee.py) class which inherits from it and it also a blueprint for internal employees, in this way we are open for having new employee types, and avoid change in the code. Currently, the application has [Agent](src/users/agent.py) and [Manager](src/users/manager.py) employees. Additionally, it has a [customer](src/users/customer.py) class which is directly inherited from [BaseUser](src/users/base_user.py) and represents a customer who reserves and rents a car.
    ```
    BaseUser (Abstract)
    ├── Employee (Abstract)
    │   ├── Agent (Concrete)
    │   └── Manager (Concrete)
    └── Customer (Concrete)
    ```
   
2. **Branch:** [Branch](src/branch/branch.py) represents a branch of the company and implemented as a normal class because it does not have different types.
    ```
    Branch (Concrete)
    ```
3. **Vehicle, VehicleClass & MaintenanceRecord:** [VehicleClass](src/vehicle/vehicle_class.py), [Vehicle](src/vehicle/vehicle.py), and [MaintenanceRecord](src/vehicle/maintenance_record.py) are normal classes, there is a relationship between them because Vehicle is classified as a VehicleClass, and Vehicle has a list of MaintenanceRecords.
    ```
    VehicleClass (Concrete)
    Vehicle (Concrete)
    MaintenanceRecord (Concrete)
    ```
4. **Reservation, Invoice, AddOn, and InsuranceTier**: [Reservation](src/reservation/reservation.py), [Invoice](src/reservation/invoice.py), [AddOn](src/reservation/add_on.py), and [InsuranceTier](src/reservation/insurance_tier.py) classes are also normal concrete classes that can be initialized during the run time, I could implement `Decorator design pattern` for this part, but due to time limitations, I could not. But for later development Decorator is a well-suited design pattern for this part of the application.
    ```
    Reservation (Concrete)
    Invoice (Concrete)
    AddOn (Concrete)
    InsuranceTier (Concrete)
    ```
   
5. **Pricing Strategy:** for pricing strategy, I have used `Strategy design pattern` so that we can easily add new pricing strategies without changing the code. For now there are 3 pricing strategies: normal price calculation, 15% off on first reservation, and 10% off on each five reservations. The implementation has a [pricing strategy interface](src/pricing_strategy/strategy_interface.py), [concrete strategies](src/pricing_strategy/concrete_strategies.py), and [pricing strategy](src/pricing_strategy/pricing_strategy.py) which decides which strategy to use.
    ```
    StrategyInterface (Abstract Strategy)
    ├── DailyPricingStrategy (Concrete Strategy)
    ├── LoyaltyStrategy (Concrete Strategy)
    └── FirstOrderStrategy (Concrete Strategy)
   
    PricingStrategy (Concrete Context)
    ```
   
6. **Payment:** For payments, I have used `Factory design pattern` since we have creditcard and PayPal right now, but we might add cryptocurrency payment later or other providers such as Stripe. I have defined a [product interface](src/payment/product_interface.py), [concrete products](src/payment/concrete_products.py), [factory interface](src/payment/factory_interface.py), and finally [concrete factories](src/payment/concrete_factories.py). With Factory pattern, we are always open to new payment methods without changing the code we already have.
    ```
    PaymentInterface (Abstract Product)
    ├── CreditCard (Concrete Product)
    └── PayPal (Concrete Product)
   
    PaymentFactoryInterface (Abstract Factory)
    ├── CreditCardFactory (Concrete Factory)
    └── PayPalFactory (Concrete Factory)
    ```
   
7. **Notification:** For the notification system, I have used `Observer design pattern`. This design pattern helped me to design a subscription mechanism to notify different `BaseUsers` about specific events related to them. For notification system I have implemented [NotificationManagerInterface](src/notification/notification_manager_interface.py) which is a blueprint for [NotificationManager](src/notification/notification_manager.py) and can attach, detach, or notify to [Subscribers](src/notification/subscribers.py) that are created from [SubscriberInterface](src/notification/subscriber_interface.py).

![UML Diagram](uml/uml.png)


## 3. Business Rules
1. All users including `Customers` and `Employees` must be at least 18 years old.
2. ID of all entities are created automatically and cannot be edited later.
3. `Customers` can pay for a `Reservation` only if it has been approved by an `Agent`.
4. Having an `InsuranceTier` for the `Reservation` is mandatory.
5. Total price of all `Reservations` are calculated automatically using `PricingStrategy` and cannot be modified externally.
6. For all `Reservations`, an `Invoice` is created automatically with PENDING status.

## 4. How to Run
1. Create a virtual environment with `python -m venv .venv` and activate it with `source venv/bin/activate`.
2. Install all dependencies by running `pip install -r requirements.txt`.
3. Run `python main.py` to start the application.

> Note: [main.py](main.py) is a simple demonstration of the application. It creates a `Branch`, `Customer`, `Agent`, `VehicleClass`, and `Vehicle`. Then the customer created a `Reservation` and the application sends a notification to both customer and the agent, and after agent approves the reservation, customer pays the invoice successfully.
> To keep main.py clean, I have implemented object creation classes in [utils.py](utils.py) so [main.py](main.py) stays clean with the focus on application logic.

