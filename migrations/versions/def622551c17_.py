"""empty message

Revision ID: def622551c17
Revises: 6d004986462e
Create Date: 2018-11-27 02:07:51.377281

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'def622551c17'
down_revision = '6d004986462e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feature_requests', sa.Column('target_date', sa.DateTime(), nullable=False))
    op.drop_column('feature_requests', 'targt_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feature_requests', sa.Column('targt_date', mysql.DATETIME(), nullable=False))
    op.drop_column('feature_requests', 'target_date')
    # ### end Alembic commands ###
