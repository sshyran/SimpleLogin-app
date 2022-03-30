"""empty message

Revision ID: fc2eb1d7e4fc
Revises: 68e2f38e33f4
Create Date: 2021-05-28 19:59:04.259149

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "fc2eb1d7e4fc"
down_revision = "68e2f38e33f4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_alias_hibp_alias_id"), "alias_hibp", ["alias_id"], unique=False
    )
    op.create_index(
        op.f("ix_alias_hibp_hibp_id"), "alias_hibp", ["hibp_id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_alias_hibp_hibp_id"), table_name="alias_hibp")
    op.drop_index(op.f("ix_alias_hibp_alias_id"), table_name="alias_hibp")
    # ### end Alembic commands ###
