from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse  # optional if you want redirects

from app.core.database import Base, engine
from app.api import customer_routes, ticket_routes
from sqlalchemy import text

# Create DB tables on startup (simple demo/prototype approach).
# In production, prefer Alembic migrations.
Base.metadata.create_all(bind=engine)

# Lightweight SQLite migration: ensure 'severity' column exists on 'tickets'
try:
  if engine.url.get_backend_name() == "sqlite":
    with engine.begin() as conn:
      cols = conn.execute(text("PRAGMA table_info('tickets')")).fetchall()
      col_names = {row[1] for row in cols}
      if "severity" not in col_names:
        conn.execute(text("ALTER TABLE tickets ADD COLUMN severity TEXT NOT NULL DEFAULT 'low'"))
except Exception:
  # Best-effort; skip if migration fails (e.g., during first run before table exists)
  pass

app = FastAPI(title="Simple Helpdesk CRM")

# Jinja2 templates directory
templates = Jinja2Templates(directory="app/templates")

app.include_router(customer_routes.router, prefix="/customers", tags=["Customers"])
app.include_router(ticket_routes.router, prefix="/tickets", tags=["Tickets"])

@app.get("/", include_in_schema=False)
def index(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health_check():
  return {"status": "ok"}
