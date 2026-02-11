from sqlalchemy.orm import Session

from app.models.ticket import Ticket


def create_ticket(db: Session, title: str, description: str, customer_id: int, severity: str):
    ticket = Ticket(
        title=title,
        description=description,
        severity=severity,
        customer_id=customer_id,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_all_tickets(db: Session):
    return db.query(Ticket).all()
