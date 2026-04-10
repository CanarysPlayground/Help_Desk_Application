# Simple Helpdesk CRM

> **Audience:** Developers &nbsp;|&nbsp; **Stack:** FastAPI, SQLAlchemy, SQLite, Python 3.11+ &nbsp;|&nbsp; **Pre-requisites:** Python 3.11+, Git, VS Code

---

## What You Will Build

A production-structured CRM/Helpdesk backend built with **FastAPI** and **SQLAlchemy**. The application exposes a RESTful API for managing customers and support tickets with a clean layered architecture.

| Capability | Description |
|---|---|
| Customer Management | Full CRUD for customer records |
| Ticket Management | Create, update, and resolve support tickets |
| Layered Architecture | Routes → Services → Repositories → Models |
| RESTful API | Auto-documented endpoints via FastAPI + Swagger UI |
| SQLite Database | Lightweight persistent storage with SQLAlchemy ORM |

---

## Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [Git CLI](https://git-scm.com/install/)
- [VS Code](https://code.visualstudio.com/download) with the GitHub Copilot Chat extension
- GitHub Copilot subscription (Individual, Business, or Enterprise)

---

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/CanarysPlayground/Help_Desk_Application.git
cd Help_Desk_Application
```

**2. Install dependencies**

```bash
# Windows (preferred):
py -m pip install --user -r requirements.txt

# macOS/Linux:
python3 -m pip install --user -r requirements.txt
```

**3. Configure environment** *(optional)*

```bash
# Windows:
copy .env.example .env

# macOS/Linux:
cp .env.example .env
```

**4. Start the server**

```bash
# Windows (preferred):
py -m uvicorn app.main:app --reload

# macOS/Linux:
python3 -m uvicorn app.main:app --reload
```

**5. Open API docs**

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

## Project Structure

```
Help_Desk_Application/
├── INSTRUCTIONS.md
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── customer_routes.py
│   │   └── ticket_routes.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   ├── customer.py
│   │   └── ticket.py
│   ├── repositories/
│   │   ├── customer_repository.py
│   │   └── ticket_repository.py
│   ├── schemas/
│   │   ├── customer.py
│   │   └── ticket.py
│   ├── services/
│   │   ├── customer_service.py
│   │   └── ticket_service.py
│   └── templates/
│       └── index.html
└── tests/
    └── test_health.py
```

---

## Key Features Covered

| Feature | Description |
|---|---|
| FastAPI | High-performance async web framework with automatic OpenAPI docs |
| SQLAlchemy ORM | Declarative models with session-scoped database access |
| Layered Architecture | Clean separation of routes, services, repositories, and models |
| Pydantic Schemas | Request/response validation with type-safe schemas |
| SQLite | Zero-config local database, swappable for PostgreSQL in production |

---

## Further Learning

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/install-copilot-cli)

> **Note:** For production use, consider adding JWT authentication, pagination, and replacing SQLite with PostgreSQL.