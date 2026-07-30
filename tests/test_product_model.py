import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.base import Base
from app.models.product import Product


@pytest.fixture
def db_session() -> Session:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    Base.metadata.drop_all(engine)


def test_product_upc_preserves_leading_zeros(db_session: Session) -> None:
    product = Product(upc="001234567890", name="Sample Lager", category="Beer")
    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    assert product.upc == "001234567890"


@pytest.mark.parametrize("field", ["upc", "name", "category"])
def test_product_required_fields_are_not_nullable(db_session: Session, field: str) -> None:
    payload = {"upc": "123456789012", "name": "Sample Wine", "category": "Wine"}
    payload[field] = None

    db_session.add(Product(**payload))

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_product_upc_must_be_unique(db_session: Session) -> None:
    first = Product(upc="777777777777", name="First Product", category="Beer")
    second = Product(upc="777777777777", name="Second Product", category="Wine")

    db_session.add(first)
    db_session.commit()
    db_session.add(second)

    with pytest.raises(IntegrityError):
        db_session.commit()
