"""added owners

Revision ID: 0faec84ee1a4
Revises: 5d58ba75897c
Create Date: 2023-08-22 15:37:08.659713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0faec84ee1a4'
down_revision = '5d58ba75897c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner')
    # ### end Alembic commands ###
