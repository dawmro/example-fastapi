"""add created_at to posts table

Revision ID: e411ab4db69b
Revises: 8a4c5edbd4fd
Create Date: 2022-10-13 09:39:56.744439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e411ab4db69b'
down_revision = '8a4c5edbd4fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                    server_default=sa.text('current_timestamp'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    pass
