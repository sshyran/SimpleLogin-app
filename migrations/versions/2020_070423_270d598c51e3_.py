"""empty message

Revision ID: 270d598c51e3
Revises: 7128f87af701
Create Date: 2020-07-04 23:32:25.297082

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "270d598c51e3"
down_revision = "7128f87af701"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "public_domain",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=False
        ),
        sa.Column(
            "updated_at", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True
        ),
        sa.Column("domain", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("domain"),
    )
    op.add_column(
        "users",
        sa.Column("default_random_alias_public_domain_id", sa.Integer(), nullable=True),
    )
    op.drop_constraint(
        "users_default_random_alias_domain_id_fkey", "users", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "users",
        "custom_domain",
        ["default_random_alias_domain_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        None,
        "users",
        "public_domain",
        ["default_random_alias_public_domain_id"],
        ["id"],
        ondelete="SET NULL",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="foreignkey")
    op.drop_constraint(None, "users", type_="foreignkey")
    op.create_foreign_key(
        "users_default_random_alias_domain_id_fkey",
        "users",
        "custom_domain",
        ["default_random_alias_domain_id"],
        ["id"],
    )
    op.drop_column("users", "default_random_alias_public_domain_id")
    op.drop_table("public_domain")
    # ### end Alembic commands ###
