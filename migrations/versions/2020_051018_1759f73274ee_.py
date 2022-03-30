"""empty message

Revision ID: 1759f73274ee
Revises: bf11ab2f0a7a
Create Date: 2020-05-10 18:33:55.376369

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1759f73274ee"
down_revision = "bf11ab2f0a7a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "email_log", sa.Column("bounced_mailbox_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None, "email_log", "mailbox", ["bounced_mailbox_id"], ["id"], ondelete="cascade"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "email_log", type_="foreignkey")
    op.drop_column("email_log", "bounced_mailbox_id")
    # ### end Alembic commands ###
