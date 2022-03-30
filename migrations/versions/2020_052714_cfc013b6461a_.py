"""empty message

Revision ID: cfc013b6461a
Revises: 4a7d35941602
Create Date: 2020-05-27 14:11:16.016417

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "cfc013b6461a"
down_revision = "4a7d35941602"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "alias",
        sa.Column(
            "cannot_be_disabled", sa.Boolean(), server_default="0", nullable=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("alias", "cannot_be_disabled")
    # ### end Alembic commands ###
