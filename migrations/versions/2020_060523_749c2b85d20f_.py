"""empty message

Revision ID: 749c2b85d20f
Revises: b2d51e4d94c8
Create Date: 2020-06-05 23:10:18.164302

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "749c2b85d20f"
down_revision = "b2d51e4d94c8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "directory_mailbox",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("directory_id", sa.Integer(), nullable=False),
        sa.Column("mailbox_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["directory_id"], ["directory.id"], ondelete="cascade"),
        sa.ForeignKeyConstraint(["mailbox_id"], ["mailbox.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("directory_id", "mailbox_id", name="uq_directory_mailbox"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("directory_mailbox")
    # ### end Alembic commands ###
