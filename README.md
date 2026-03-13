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

---

## Example API Endpoints

POST /auth/register
POST /auth/login

POST /deliveries
GET /deliveries/{id}

POST /drivers/accept

---

## Project Status

Currently in development.
Building step-by-step to demonstrate backend architecture and system design.
