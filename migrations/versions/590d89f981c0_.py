"""empty message

Revision ID: 590d89f981c0
Revises: b20ee72fd9a4
Create Date: 2019-07-01 21:46:58.613910

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "590d89f981c0"
down_revision = "b20ee72fd9a4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("promo_codes", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "promo_codes")
    # ### end Alembic commands ###
