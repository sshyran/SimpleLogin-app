"""empty message

Revision ID: 75093e7ded27
Revises: e3cb44b953f2
Create Date: 2020-02-27 22:26:25.068117

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "75093e7ded27"
down_revision = "e3cb44b953f2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "social_auth",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("social", sa.String(length=128), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "social", name="uq_social_auth"),
    )
    op.alter_column(
        "users", "password", existing_type=sa.VARCHAR(length=128), nullable=True
    )
    op.alter_column(
        "users", "salt", existing_type=sa.VARCHAR(length=128), nullable=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "salt", existing_type=sa.VARCHAR(length=128), nullable=False
    )
    op.alter_column(
        "users", "password", existing_type=sa.VARCHAR(length=128), nullable=False
    )
    op.drop_table("social_auth")
    # ### end Alembic commands ###
