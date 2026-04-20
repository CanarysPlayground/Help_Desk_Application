# Stage 1: CLI Analysis — "Tickets not getting created"

> **Related Exercise:** [Exercise 1: Create Custom CLI Agent](exercises/EXERCISE_1_CLI_AGENT.md)

Goal: Diagnose and document why tickets appear not to be created.

## Quick Repro (with app running)
```powershell
# Create a customer
curl -s -X POST http://localhost:8000/customers/ `
  -H "Content-Type: application/json" `
  -d "{\"name\":\"Jane\",\"email\":\"jane@example.com\"}"

# Create a ticket (replace 1 with returned customer id)
curl -s -X POST http://localhost:8000/tickets/ `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Login Issue\",\"description\":\"Cannot login\",\"customer_id\":1,\"severity\":\"low\"}"
```
Expected symptom: 422/500 response complaining about response validation for `ticket_id`.

## CLI Steps to Diagnose and Document
- Identify mismatch in schema vs model (`ticket_id` vs `id`).
- Reproduce via curl (above) and capture responses.
- Inspect DB rows to confirm commits despite 422/500.
- Record findings in an analysis markdown file.

## Install Copilot CLI
- Reference: https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli
- Install (Windows/macOS/Linux):
  - Windows (PowerShell):
    - Use GitHub CLI `gh` (recommended), then enable Copilot CLI: see docs.
  - macOS/Linux:
    - Follow package instructions in the docs; ensure `gh` and Copilot CLI plugins are configured.

## Create Analysis File (.md)
- Create `workshop/CLI_TICKET_ANALYSIS.md` summarizing the issue, repro, root cause, and fix.
- Include DB check output and the corrected schema mapping.

> We use CLI agents whenever we want to improve developer workflow or extend backend structure without coding everything manually.

## Code Trace (for context)
- Route: app/api/ticket_routes.py posts TicketCreate, returns TicketResponse.
- Service/Repo: app/services/ticket_service.py → app/repositories/ticket_repository.py does db.add(), db.commit(), db.refresh().
- Model: app/models/ticket.py defines `id` (primary key) and `severity`.
- Schema: app/schemas/ticket.py `TicketResponse` currently uses `ticket_id`.

## Root Cause
- `TicketResponse.ticket_id` does not match the SQLAlchemy model attribute `id`. With `from_attributes = True`, Pydantic expects field names to match model attributes, causing response validation errors even when DB commits succeed.

## Fix Options
- Preferred: Change `TicketResponse.ticket_id` to `id` in app/schemas/ticket.py.
- Alternative: In the route, return a dict mapping `ticket_id: ticket.id` and adjust other fields explicitly.

## Sanity Check (DB)
```powershell
python - <<'PY'
from sqlalchemy import create_engine, text
from app.core.config import settings
engine = create_engine(settings.DATABASE_URL)
with engine.begin() as conn:
    print(conn.execute(text("SELECT id,title,severity,customer_id FROM tickets")).fetchall())
PY
```

## What CLI agents can improve
- Discovery: Use rg to instantly find mismatches (`ticket_id` vs `id`).
- Repro: Script curl flows to consistently reproduce API behavior.
- DB grep: Lightweight SQL checks without heavy tooling.
- Diff hints: Generate suggested patches quickly.
- Guardrails: Pre-flight checks before changing code (lint/format/test).

## References
- FastAPI (Response Models): https://fastapi.tiangolo.com/tutorial/response-model/
- Pydantic v2 (from_attributes): https://docs.pydantic.dev/latest/concepts/serialization/#from-attributes
- SQLAlchemy 2.0 ORM: https://docs.sqlalchemy.org/en/20/orm/
- Copilot CLI: https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli
