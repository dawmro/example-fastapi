"""add foreign-key to posts table

Revision ID: 0119c07c2cdf
Revises: 25e6c28e11c6
Create Date: 2022-10-13 02:23:05.768450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0119c07c2cdf'
down_revision = '25e6c28e11c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=True))
    with op.batch_alter_table('posts') as batch_op:
        batch_op.create_foreign_key('post_user_fk', referent_table='users', local_cols=['owner_id'], 
                                    remote_cols=['id'], ondelete='CASCADE')

    #op.create_foreign_key('post_user_fk', source_table='posts', referent_table='users', local_cols=['owner_id'],
    #                      remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
