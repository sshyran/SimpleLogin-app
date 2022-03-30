"""empty message

Revision ID: 6cc7f073b358
Revises: 5c77d685df87
Create Date: 2021-05-17 21:26:15.007317

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "6cc7f073b358"
down_revision = "5c77d685df87"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hibp",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_hibp_name"), "hibp", ["name"], unique=True)
    op.create_table(
        "alias_hibp",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("alias_id", sa.Integer(), nullable=True),
        sa.Column("hibp_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["alias_id"],
            ["alias.id"],
        ),
        sa.ForeignKeyConstraint(
            ["hibp_id"],
            ["hibp.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("alias_id", "hibp_id", name="uq_alias_hibp"),
    )
    op.add_column(
        "alias",
        sa.Column(
            "hibp_last_check", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("alias", "hibp_last_check")
    op.drop_table("alias_hibp")
    op.drop_index(op.f("ix_hibp_name"), table_name="hibp")
    op.drop_table("hibp")
    # ### end Alembic commands ###
