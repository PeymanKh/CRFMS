# Car Rental & Fleet Management System (CRFMS)

> This project is implementation of a Car Rental & Fleet Management System for advanced python course. I strongly suggest reading this README.md file to fully understand my approach and design system. 

## 1. Introduction
The main goal of this project is to create a CRFMS system with respect to SOLID principles and GoF design patterns. *Factory Method*, *Template Method*, *Observer*, and *Strategy* design patterns are used to solve specific architectural challenges. In this document I will explain all entities used in the project, the reason behind my design, and relationship between them.

## 2. Design Philosophy
1. **Users:** User (person) is the first entity in the system. For designing all users including customers and employees, I inspired by LangChain API design. It has a base class for everything then expanded those base classes to create specific objects. For example, it has a BaseMessage class which is a blueprint of creating messages in the ecosystem and different kind of messages such as AIMessage, UserMessage, ToolMessage, etc. So in my design I have defined a [BaseUser](src/users/base_user.py) class, which is a blueprint for all different kinds of users envolved in the application. Then, I created an [Employee](src/users/employee.py) class which inherits from it and it also a blueprint for internal employees, in this way we are open for having new employee types, and avoid change in the code. Currently, we have [Agent](src/users/agent.py) and [Manager](src/users/manager.py). Additionally we have a [customer](src/users/customer.py) class which is directly inherited from [BaseUser](src/users/base_user.py).
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