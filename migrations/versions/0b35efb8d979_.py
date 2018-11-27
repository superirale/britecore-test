"""empty message

Revision ID: 0b35efb8d979
Revises: def622551c17
Create Date: 2018-11-27 02:51:15.064588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b35efb8d979'
down_revision = 'def622551c17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('priority', table_name='feature_requests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('priority', 'feature_requests', ['priority'], unique=True)
    # ### end Alembic commands ###
