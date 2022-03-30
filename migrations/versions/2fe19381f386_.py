"""empty message

Revision ID: 2fe19381f386
Revises: d03e433dc248
Create Date: 2019-07-01 11:47:24.934574

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2fe19381f386"
down_revision = "d03e433dc248"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("is_developer", sa.Boolean(), server_default="0", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_developer")
    # ### end Alembic commands ###
