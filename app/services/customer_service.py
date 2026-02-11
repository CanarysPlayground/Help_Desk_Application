from sqlalchemy.orm import Session

from app.repositories import customer_repository


def create_customer(db: Session, name: str, email: str):
    return customer_repository.create_customer(db, name, email)


def list_customers(db: Session):
    return customer_repository.get_all_customers(db)
