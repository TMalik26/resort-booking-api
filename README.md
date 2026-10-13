# Resort Booking API

A RESTful API for managing rental properties, property images, availability, pricing periods, and bookings. Built with Django and Django REST Framework.

## Overview

Resort Booking API is the backend for a property rental website. It provides endpoints for retrieving property information, displaying photo galleries, managing availability, and handling booking-related data.

The project is designed to support both public access to property information and administrative management of rental properties.

## Features

- **Property management** — store property details, including names, descriptions, addresses, and slugs.
- **Property image galleries** — associate multiple images with each property and control their display order.
- **Availability management** — represent bookings and blocked periods for each property.
- **Pricing management** — define prices for specific date ranges.
- **REST API** — expose structured JSON data through Django REST Framework.
- **Automated checks** — run code quality checks and tests through GitHub Actions.

## Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Supabase Storage** — property image storage
- **pytest / pytest-django** — automated testing
- **Ruff** — linting and code formatting
- **GitHub Actions** — CI

## Data Models

The backend is organized around the following entities:

| Model | Description |
|---|---|
| `Property` | Stores information about a rental property. |
| `PropertyImage` | Stores image references and display order for a property. |
| `Booking` | Represents a booking associated with a property. |
| `BlockedPeriod` | Represents a period when a property is unavailable. |
| `PricePeriod` | Defines pricing for a specific date range. |

Each property can have multiple images, bookings, blocked periods, and pricing periods.

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── backend.yml
├── backend/
│   ├── config/
│   ├── users/
│   ├── manage.py
│   ├── requirements.txt
│   ├── pytest.ini
│   └── pyproject.toml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create and activate a virtual environment

From the repository root:

```bash
python -m venv backend/venv
```

On Windows PowerShell:

```powershell
backend\venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source backend/venv/bin/activate
```

### 3. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the `backend/` directory and configure the variables required by the Django settings.

Typical settings include:

```dotenv
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your_database
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
```

Configure the Supabase Storage credentials and other environment variables if required by the project settings.

**Important:** Do not commit `.env` files, secret keys, or storage credentials to version control.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

Available endpoints depend on the URL configuration.

## Testing

Run the automated test suite from the `backend/` directory:

```bash
pytest
```

## Code Quality

Run Ruff to check the code:

```bash
ruff check .
```

Check code formatting:

```bash
ruff format --check .
```

Format the code:

```bash
ruff format .
```

## Continuous Integration

GitHub Actions runs backend checks when relevant backend files or the workflow configuration change.

The workflow includes:

- Installing Python dependencies
- Applying database migrations
- Running Ruff lint checks
- Verifying code formatting
- Running automated tests

## Development Workflow

The project uses a branch-based Git workflow:

- `main` — stable code
- `dev` — integration branch
- `feat/*` — feature branches

Features are developed in separate branches and merged into `dev` before being integrated into `main`.

## Project Status

The backend is under active development. Features and integrations may evolve as the project progresses.

## License

No license has been specified yet.