"""empty message

Revision ID: e99989e6ad56
Revises: 7c0dbd378cdb
Create Date: 2021-01-04 14:31:12.163039

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e99989e6ad56"
down_revision = "7c0dbd378cdb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("email_log", sa.Column("spam_report", sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("email_log", "spam_report")
    # ### end Alembic commands ###
