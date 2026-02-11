from sqlalchemy.orm import Session

from app.repositories import ticket_repository


def create_ticket(db: Session, title: str, description: str, customer_id: int, severity: str):
    return ticket_repository.create_ticket(db, title, description, customer_id, severity)


def list_tickets(db: Session):
    return ticket_repository.get_all_tickets(db)
