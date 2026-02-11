from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services import ticket_service

router = APIRouter()


@router.post("/", response_model=TicketResponse)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db)):
    return ticket_service.create_ticket(
        db,
        payload.title,
        payload.description,
        payload.customer_id,
        payload.severity.value if hasattr(payload.severity, "value") else str(payload.severity),
    )


@router.get("/", response_model=list[TicketResponse])
def list_tickets(db: Session = Depends(get_db)):
    return ticket_service.list_tickets(db)
