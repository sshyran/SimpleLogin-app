"""empty message

Revision ID: e11c3dd48a6f
Revises: 48b991e9de06
Create Date: 2021-04-01 12:35:04.944100

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e11c3dd48a6f"
down_revision = "48b991e9de06"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "authorization_code",
        sa.Column("nonce", sa.Text(), server_default=sa.text("NULL"), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("authorization_code", "nonce")
    # ### end Alembic commands ###
