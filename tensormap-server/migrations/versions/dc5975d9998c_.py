"""empty message

Revision ID: dc5975d9998c
Revises: cb58c1cf5202
Create Date: 2024-08-23 09:58:26.673199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc5975d9998c'
down_revision = 'cb58c1cf5202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('model_basic', 'target_field',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('model_basic', 'target_field',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###