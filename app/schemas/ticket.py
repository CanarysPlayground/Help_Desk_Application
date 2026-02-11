from enum import Enum
from pydantic import BaseModel


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class TicketCreate(BaseModel):
    title: str
    description: str
    customer_id: int
    severity: Severity = Severity.low


class TicketResponse(BaseModel):
    ticket_id: int
    title: str
    description: str
    status: str
    severity: Severity
    customer_id: int

    class Config:
        from_attributes = True
