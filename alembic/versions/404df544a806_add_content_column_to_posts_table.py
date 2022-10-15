"""add content column to posts table

Revision ID: 404df544a806
Revises: cb885126dcc4
Create Date: 2022-10-09 07:35:59.986692

"""
from wsgiref import headers
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '404df544a806'
down_revision = 'cb885126dcc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    with op.batch_alter_table('posts') as batch_op:
        batch_op.drop_column('content')
    pass
