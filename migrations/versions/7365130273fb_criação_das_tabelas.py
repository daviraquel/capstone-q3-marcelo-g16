"""criação das tabelas

Revision ID: 7365130273fb
Revises: 
Create Date: 2022-04-29 18:49:59.457766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7365130273fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('categories_collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nfts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('for_sale', sa.Boolean(), nullable=False),
    sa.Column('value', sa.Numeric(), nullable=False),
    sa.Column('description', sa.String(length=50), nullable=False),
    sa.Column('collection', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['collection'], ['collections.id'], ),
    sa.ForeignKeyConstraint(['creator'], ['users.id'], ),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seller', sa.Integer(), nullable=False),
    sa.Column('buyer', sa.Integer(), nullable=False),
    sa.Column('item', sa.Integer(), nullable=False),
    sa.Column('value', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['buyer'], ['users.id'], ),
    sa.ForeignKeyConstraint(['item'], ['nfts.id'], ),
    sa.ForeignKeyConstraint(['seller'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    op.drop_table('nfts')
    op.drop_table('categories_collections')
    op.drop_table('users')
    op.drop_table('collections')
    op.drop_table('categories')
    # ### end Alembic commands ###
