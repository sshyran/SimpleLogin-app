"""empty message

Revision ID: 5e868298fee7
Revises: 0b28518684ae
Create Date: 2019-12-02 00:28:40.281432

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5e868298fee7"
down_revision = "0b28518684ae"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "gen_email", sa.Column("custom_domain_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None,
        "gen_email",
        "custom_domain",
        ["custom_domain_id"],
        ["id"],
        ondelete="cascade",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "gen_email", type_="foreignkey")
    op.drop_column("gen_email", "custom_domain_id")
    # ### end Alembic commands ###
