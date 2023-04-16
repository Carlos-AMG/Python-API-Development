"""add content column to posts table

Revision ID: d4b5f2dacb50
Revises: 33143b459434
Create Date: 2023-04-15 14:49:01.626696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b5f2dacb50'
down_revision = '33143b459434'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
