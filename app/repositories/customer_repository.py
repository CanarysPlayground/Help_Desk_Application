from sqlalchemy.orm import Session

from app.models.customer import Customer


def create_customer(db: Session, name: str, email: str):
    customer = Customer(name=name, email=email)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def get_all_customers(db: Session):
    return db.query(Customer).all()
