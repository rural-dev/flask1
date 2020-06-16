"""Adding tag columnn to page

Revision ID: 3795b7ba9e29
Revises: 0eb01c197d66
Create Date: 2020-06-16 00:36:03.661982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3795b7ba9e29'
down_revision = '0eb01c197d66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page', sa.Column('tag', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('page', 'tag')
    # ### end Alembic commands ###
