"""empty message

Revision ID: ad467baf7ec8
Revises: 4b483a762fed
Create Date: 2021-12-02 16:32:50.884324

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "ad467baf7ec8"
down_revision = "4b483a762fed"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "phone_country",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "phone_number",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("country_id", sa.Integer(), nullable=False),
        sa.Column("number", sa.String(length=128), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["country_id"], ["phone_country.id"], ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("number"),
    )
    op.create_table(
        "phone_message",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("number_id", sa.Integer(), nullable=False),
        sa.Column("from_number", sa.String(length=128), nullable=False),
        sa.Column("body", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["number_id"], ["phone_number.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "phone_reservation",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("number_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("start", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
        sa.Column("end", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
        sa.ForeignKeyConstraint(["number_id"], ["phone_number.id"], ondelete="cascade"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "users",
        sa.Column("can_use_phone", sa.Boolean(), server_default="0", nullable=False),
    )
    op.add_column("users", sa.Column("phone_quota", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "phone_quota")
    op.drop_column("users", "can_use_phone")
    op.drop_table("phone_reservation")
    op.drop_table("phone_message")
    op.drop_table("phone_number")
    op.drop_table("phone_country")
    # ### end Alembic commands ###
