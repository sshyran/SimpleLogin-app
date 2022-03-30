"""empty message

Revision ID: 48b991e9de06
Revises: 517b79c56088
Create Date: 2021-04-01 12:31:10.306328

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "48b991e9de06"
down_revision = "517b79c56088"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "client_user",
        sa.Column("nonce", sa.Text(), server_default=sa.text("NULL"), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("client_user", "nonce")
    # ### end Alembic commands ###
