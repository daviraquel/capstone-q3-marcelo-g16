"""criaçao last_deposit

Revision ID: 029e4912c8d9
Revises: 5d6556fdbf31
Create Date: 2022-05-04 11:54:01.108508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '029e4912c8d9'
down_revision = '5d6556fdbf31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_deposit', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_deposit')
    # ### end Alembic commands ###
