"""criado password hash

Revision ID: 661ba13ee444
Revises: 7365130273fb
Create Date: 2022-05-02 19:29:45.674917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "661ba13ee444"
down_revision = "7365130273fb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("password_hash", sa.String(length=511), nullable=False)
    )
    op.drop_column("users", "password")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "password", sa.VARCHAR(length=20), autoincrement=False, nullable=False
        ),
    )
    op.drop_column("users", "password_hash")
    # ### end Alembic commands ###
