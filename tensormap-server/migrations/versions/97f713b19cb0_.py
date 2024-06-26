"""empty message

Revision ID: 97f713b19cb0
Revises: 
Create Date: 2024-06-14 16:44:39.798623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97f713b19cb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_file',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.String(length=100), nullable=False),
    sa.Column('file_type', sa.String(length=10), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('data_process',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('target', sa.String(length=50), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['data_file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model_basic',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model_name', sa.String(length=50), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('model_type', sa.Integer(), nullable=False),
    sa.Column('target_field', sa.String(length=50), nullable=False),
    sa.Column('training_split', sa.Float(), nullable=False),
    sa.Column('optimizer', sa.String(length=50), nullable=False),
    sa.Column('metric', sa.String(length=50), nullable=False),
    sa.Column('epochs', sa.Integer(), nullable=False),
    sa.Column('loss', sa.String(length=50), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['data_file.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model_name')
    )
    op.create_table('model_configs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('parameter', sa.String(length=50), nullable=False),
    sa.Column('value', sa.String(length=50), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['model_id'], ['model_basic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model_results',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('epoc', sa.Integer(), nullable=False),
    sa.Column('iteration', sa.Integer(), nullable=False),
    sa.Column('metric', sa.String(length=50), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['model_id'], ['model_basic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model_results')
    op.drop_table('model_configs')
    op.drop_table('model_basic')
    op.drop_table('data_process')
    op.drop_table('data_file')
    # ### end Alembic commands ###
