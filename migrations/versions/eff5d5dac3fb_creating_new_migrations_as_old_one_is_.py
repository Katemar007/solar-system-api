"""Creating new migrations as old one is broken

Revision ID: eff5d5dac3fb
Revises: 
Create Date: 2025-05-06 13:28:30.490185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eff5d5dac3fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('habitable', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('moon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('orbit_period', sa.String(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moon')
    op.drop_table('planet')
    # ### end Alembic commands ###
