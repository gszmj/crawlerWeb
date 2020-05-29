"""empty message

Revision ID: 3a3bd3eac5c2
Revises: 
Create Date: 2020-04-23 20:50:22.534201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a3bd3eac5c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dytt',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=24), nullable=True),
    sa.Column('classify', sa.String(length=10), nullable=True),
    sa.Column('title', sa.String(length=24), nullable=True),
    sa.Column('date', sa.String(length=10), nullable=True),
    sa.Column('size', sa.String(length=8), nullable=True),
    sa.Column('introduction', sa.String(length=32), nullable=True),
    sa.Column('magnet', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dytt')
    # ### end Alembic commands ###