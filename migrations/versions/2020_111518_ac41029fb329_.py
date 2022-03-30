"""empty message

Revision ID: ac41029fb329
Revises: 9dc16e591f88
Create Date: 2020-11-15 18:37:11.158507

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ac41029fb329"
down_revision = "9dc16e591f88"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "alias", sa.Column("pinned", sa.Boolean(), server_default="0", nullable=False)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("alias", "pinned")
    # ### end Alembic commands ###
