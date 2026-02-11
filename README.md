# Simple Helpdesk CRM

A simple production-structured CRM/Helpdesk backend built with FastAPI.

## Features

- Customer management
- Ticket management
- Layered architecture
- SQLite database
- Clean project structure

## Run the app

# 1) Install dependencies (no virtualenv)

# Windows (preferred):
py -m pip install --user -r requirements.txt

# macOS/Linux:
python3 -m pip install --user -r requirements.txt

# 2) Configure environment (optional)
# Windows:
copy .env.example .env
# macOS/Linux:
cp .env.example .env

# 3) Start the server
# Windows (preferred):
py -m uvicorn app.main:app --reload
# macOS/Linux:
python3 -m uvicorn app.main:app --reload

# Open API docs:
# http://127.0.0.1:8000/docs


helpdesk_app/
├── INSTRUCTIONS.md
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── __pycache__/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── customer_routes.py
│   │   ├── ticket_routes.py
│   │   └── __pycache__/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── __pycache__/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── customer.py
│   │   ├── ticket.py
│   │   └── __pycache__/
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── customer_repository.py
│   │   ├── ticket_repository.py
│   │   └── __pycache__/
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── customer.py
│   │   ├── ticket.py
│   │   └── __pycache__/
│   ├── services/
│   │   ├── __init__.py
│   │   ├── customer_service.py
│   │   ├── ticket_service.py
│   │   └── __pycache__/
│   └── templates/
│       └── index.html
├── tests/
│   └── test_health.py
└── WorkShop/