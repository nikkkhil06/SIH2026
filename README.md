# GreenFleetQ Backend

Backend API for **SIH 2026 Problem Statement 26138 – Quantum-Inspired Fuel Consumption Prediction and Green Fleet Optimization**.

The backend is developed using **Python, FastAPI, PostgreSQL, SQLAlchemy, and Pydantic**. It provides REST APIs for vessel data, fuel data, operational data, environmental data, fuel prediction, and fleet optimization.

## Project Objective

GreenFleetQ aims to help optimize vessel operations by:

* Predicting vessel fuel consumption
* Selecting suitable vessels and fuel configurations
* Optimizing fleet operations based on cargo demand, distance, and time constraints
* Reducing fuel consumption, operational cost, and emissions
* Integrating a quantum-inspired fleet optimization approach

## Technology Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn
* python-dotenv

## Project Structure

```text
app/
├── core/
│   ├── config.py
│   └── security.py
│
├── database/
│   ├── connection.py
│   └── dependencies.py
│
├── models/
│   ├── environmental_data.py
│   ├── fuel_prediction.py
│   ├── fuel_types.py
│   ├── operational_data.py
│   ├── optimization_result.py
│   ├── optimization_scenario.py
│   └── vessels.py
│
├── routers/
│   ├── environmental_data.py
│   ├── fuel_prediction.py
│   ├── fuels.py
│   ├── operational_data.py
│   ├── optimization.py
│   ├── prediction.py
│   └── vessels.py
│
├── schemas/
│   ├── environmental_data.py
│   ├── fuel.py
│   ├── fuel_prediction.py
│   ├── operational_data.py
│   ├── optimization.py
│   ├── prediction.py
│   ├── results.py
│   └── vessels.py
│
├── services/
│   └── prediction_service.py
│
├── utils/
│   └── helpers.py
│
└── main.py
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nikkkhil06/SIH2026.git
cd SIH2026
```

### 2. Switch to Backend Branch

```bash
git checkout backend-ninad
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure PostgreSQL

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/greenfleetq
```

Do not commit the `.env` file to GitHub.

## Running the Backend

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Root

```http
GET /
```

Checks whether the backend is running.

### Vessels

```http
GET /vessels/
```

Returns vessel information from the database.

### Fuel Types

```http
GET /fuel-types/
```

Returns available fuel types.

### Operational Data

```http
GET /operational-data/
```

Returns operational data.

### Environmental Data

```http
GET /environmental-data/
```

Returns environmental data.

### Historical Fuel Predictions

```http
GET /fuel-predictions/
```

Returns stored fuel prediction records.

### Fuel Prediction

```http
POST /fuel/predict
```

Provides fuel consumption prediction through the prediction service.

The current prediction integration is temporary and will be updated when the new prediction model from the ML team is ready.

### Fleet Optimization

```http
POST /optimization/
```

Creates an optimization scenario.

#### Request

```json
{
  "cargo_demand": 15000,
  "distance": 800,
  "max_time": 36,
  "objective": "balanced"
}
```

#### Supported Objectives

```text
fuel
cost
emissions
balanced
```

#### Current Response

```json
{
  "scenario_id": "SXXXXXXXX",
  "message": "Optimization scenario created successfully",
  "status": "pending"
}
```

The optimization endpoint currently creates and stores an optimization scenario. The final optimization calculation will be integrated with the ML and quantum-inspired optimizer once the updated implementation is available.

## Frontend Integration

The backend communicates with the React frontend through REST APIs.

The user provides:

* Cargo Demand
* Distance
* Maximum Time
* Objective

The frontend sends these values to:

```http
POST /optimization/
```

The backend generates a unique `scenario_id` and returns the current scenario status.

The `scenario_id` will be used for retrieving the final optimization result after the optimizer integration is completed.

## Database

PostgreSQL is used as the primary database.

SQLAlchemy is used as the ORM layer between FastAPI and PostgreSQL.

Main database entities include:

* Vessels
* Fuel Types
* Operational Data
* Environmental Data
* Fuel Predictions
* Optimization Scenarios
* Optimization Results

The database schema and data are maintained by the database team.

## Current Development Status

### Completed

* FastAPI backend setup
* PostgreSQL database connection
* SQLAlchemy integration
* Database models
* Pydantic schemas
* REST API routers
* CORS configuration
* Optimization scenario API
* Frontend API contract
* Git/GitHub backend branch

### In Progress

* Frontend ↔ Backend integration
* Final database table integration
* Optimization result API
* Updated ML prediction model integration
* Quantum-inspired fleet optimizer integration
* API testing
* Deployment

## Team Responsibilities

| Member        | Responsibility                                        |
| ------------- | ----------------------------------------------------- |
| Ninad         | Backend, FastAPI, REST APIs and integration           |
| Nikhil        | Frontend                                              |
| Meet          | PostgreSQL Database                                   |
| Aditya        | ML Prediction and Quantum-Inspired Fleet Optimization |
| Other Members | Documentation and Presentation                        |

## Important Notes

* User registration and login are not currently included because development is focused on the core system.
* Users are not required to manually select vessels or fuel types.
* Vessel and fuel selection will be handled using database information and the optimization system.
* The optimization endpoint currently returns a `pending` status until the final optimizer is integrated.
* The current fuel prediction integration will be updated with the new ML model.
* Database credentials must be stored in `.env` and must not be committed to GitHub.

## License

This project is developed as part of **Smart India Hackathon (SIH) 2026**.
