"""expand product catalog schema

Revision ID: 20260730_2045
Revises: 20260730_0025
Create Date: 2026-07-30 20:45:00.000000
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "20260730_2045"
down_revision: str | None = "20260730_0025"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("products") as batch_op:
        batch_op.add_column(sa.Column("brand", sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column("container_type", sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column("barcode_level", sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column("notes", sa.Text(), nullable=True))

    op.execute("UPDATE products SET brand = 'Unknown' WHERE brand IS NULL")

    with op.batch_alter_table("products") as batch_op:
        batch_op.alter_column("brand", existing_type=sa.String(length=255), nullable=False)
        batch_op.drop_column("distributor")


def downgrade() -> None:
    with op.batch_alter_table("products") as batch_op:
        batch_op.add_column(sa.Column("distributor", sa.String(length=255), nullable=True))
        batch_op.drop_column("notes")
        batch_op.drop_column("barcode_level")
        batch_op.drop_column("container_type")
        batch_op.drop_column("brand")
