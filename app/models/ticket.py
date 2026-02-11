from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="open")
    severity = Column(String, default="low", nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.id"))
