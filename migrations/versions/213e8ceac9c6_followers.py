"""followers

Revision ID: 213e8ceac9c6
Revises: 03e24107a748
Create Date: 2021-11-27 15:23:29.943963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '213e8ceac9c6'
down_revision = '03e24107a748'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
