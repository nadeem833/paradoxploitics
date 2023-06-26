"""Add type column to Entry table

Revision ID: 3d5e944a1b5d
Revises: 
Create Date: 2023-06-17 13:39:26.551525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d5e944a1b5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('type', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'type')
    # ### end Alembic commands ###
