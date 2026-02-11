# Setup Instructions

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



# API Usage

## Create Customer

**POST** `/customers`

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Create Ticket

**POST** `/tickets`

```json
{
  "title": "Login Issue",
  "description": "Cannot login",
  "customer_id": 1
}
```

---

# Production Improvements

- Add authentication (JWT)
- Add pagination
- Add logging
- Use PostgreSQL instead of SQLite
- Add proper playwright test suite
