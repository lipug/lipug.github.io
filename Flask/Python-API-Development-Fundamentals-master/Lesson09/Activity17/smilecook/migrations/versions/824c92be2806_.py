"""empty message

Revision ID: 824c92be2806
Revises: 6089a861042f
Create Date: 2019-11-14 16:36:45.228509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '824c92be2806'
down_revision = '6089a861042f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar_image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar_image')
    # ### end Alembic commands ###
