"""Add new userfield

Revision ID: d1cccd4272f6
Revises: 326b439606d0
Create Date: 2024-12-29 14:58:19.949564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1cccd4272f6'
down_revision = '326b439606d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner_username', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.drop_column('owner_username')

    # ### end Alembic commands ###