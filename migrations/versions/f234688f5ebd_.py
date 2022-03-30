"""empty message

Revision ID: f234688f5ebd
Revises: 213fcca48483
Create Date: 2019-06-30 18:30:55.295040

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f234688f5ebd"
down_revision = "213fcca48483"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("profile_picture_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "users", "file", ["profile_picture_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="foreignkey")
    op.drop_column("users", "profile_picture_id")
    # ### end Alembic commands ###
