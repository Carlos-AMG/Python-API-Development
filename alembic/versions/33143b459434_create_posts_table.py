"""create posts table

Revision ID: 33143b459434
Revises: 
Create Date: 2023-04-12 00:26:47.681231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33143b459434'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), 
        sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
