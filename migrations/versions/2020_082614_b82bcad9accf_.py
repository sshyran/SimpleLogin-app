"""empty message

Revision ID: b82bcad9accf
Revises: 95938a93ea14
Create Date: 2020-08-26 14:38:22.496570

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b82bcad9accf"
down_revision = "95938a93ea14"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "alias",
        sa.Column(
            "disable_email_spoofing_check",
            sa.Boolean(),
            server_default="0",
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("alias", "disable_email_spoofing_check")
    # ### end Alembic commands ###
