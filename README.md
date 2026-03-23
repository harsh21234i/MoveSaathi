# MoveSaathi
Porter-like logistics delivery backend built with FastAPI
# MoveSaathi – Logistics Delivery Backend

MoveSaathi is a backend system inspired by logistics platforms like Porter.
It allows customers to create delivery requests and drivers to accept and complete them.

The backend is built using FastAPI and follows a modular architecture suitable for real-world backend services.

---

## Features

* User authentication
* Delivery request creation
* Driver assignment
* Delivery status tracking
* Payment processing (simulation)
* RESTful API architecture

---

## Tech Stack

* FastAPI
* Python
* PostgreSQL (planned)
* SQLAlchemy
* Redis (planned for background jobs)
* Docker (planned for deployment)

---

## System Flow

Customer → API → Delivery Request → Driver Assignment → Delivery Tracking → Payment

##  Architecture Update

We introduced a Service Layer:

routes → services → database

This improves:
- Code readability
- Scalability
- Maintainability
---
##  Role-Based Access Control

Implemented role-based restrictions:

- Only customers can create deliveries
- Unauthorized roles receive 403 error

This ensures secure and realistic backend behavior.
## Example API Endpoints

POST /auth/register
POST /auth/login

POST /deliveries
GET /deliveries/{id}

POST /drivers/accept

---

##  Driver System (Phase 1)

- Driver registration implemented
- Added vehicle type and availability
- Role-based driver creation


##  Driver Availability System

- Drivers can go online/offline
- Only drivers can update status
- Availability stored in database

This enables real-time driver participation in delivery system.