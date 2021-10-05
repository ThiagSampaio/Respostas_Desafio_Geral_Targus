"""create_main_tables

Revision ID: 727a78bea4e2
Revises: 
Create Date: 2021-10-05 17:33:30.181942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '727a78bea4e2'
down_revision = None
branch_labels = None
depends_on = None

def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("data", sa.Text, nullable=False, index=True),
        sa.Column("hora", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=True)
    )

def upgrade() -> None:
    create_cleanings_table()


def downgrade() -> None:
    op.drop_table("cleanings")

