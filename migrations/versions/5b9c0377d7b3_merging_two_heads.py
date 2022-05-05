"""merging two heads

Revision ID: 5b9c0377d7b3
Revises: 7fb37baf8cff, 029e4912c8d9
Create Date: 2022-05-05 16:16:52.649895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b9c0377d7b3'
down_revision = ('7fb37baf8cff', '029e4912c8d9')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
