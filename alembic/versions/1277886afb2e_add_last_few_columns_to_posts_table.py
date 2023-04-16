"""add last few columns to posts table

Revision ID: 1277886afb2e
Revises: e6c418c3d85e
Create Date: 2023-04-15 15:43:28.624577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1277886afb2e'
down_revision = 'e6c418c3d85e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
