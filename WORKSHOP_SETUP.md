# Help Desk Workshop – Setup

Repo: Help_Desk_Application (owner: CanarysPlayground)
Default Branch: main · Current Branch: feature/severity-dropdown

Overview: A simple FastAPI app with customers and tickets, using SQLAlchemy and Pydantic. Pages served via Jinja templates; REST APIs power create/list flows.

## Prerequisites
- Python 3.11+ on Windows
- PowerShell
- Optional: gh (GitHub CLI), rg (ripgrep), curl

## Install & Run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- Health: GET http://localhost:8000/health
- UI: http://localhost:8000/

## App Structure Highlights
- API: app/api/customer_routes.py, app/api/ticket_routes.py
- Services: app/services/customer_service.py, app/services/ticket_service.py
- Repos: app/repositories/customer_repository.py, app/repositories/ticket_repository.py
- Models: app/models/customer.py, app/models/ticket.py
- Schemas: app/schemas/customer.py, app/schemas/ticket.py
- DB: app/core/database.py, app/core/config.py
