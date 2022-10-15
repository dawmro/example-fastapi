"""add last few columns to posts table

Revision ID: 8a4c5edbd4fd
Revises: 0119c07c2cdf
Create Date: 2022-10-13 09:11:37.551212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a4c5edbd4fd'
down_revision = '0119c07c2cdf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    #op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, 
                    #server_default = sa.text('current_timestamp')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    #op.drop_column('posts', 'created_at')
    pass
