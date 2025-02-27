"""5 Migration

Revision ID: ae52e29f9eb4
Revises: 8dbcd4e548c5
Create Date: 2019-07-10 16:26:31.110776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae52e29f9eb4'
down_revision = '8dbcd4e548c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('booking', 'cost')
    op.create_unique_constraint(None, 'room', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'room', type_='unique')
    op.add_column('booking', sa.Column('cost', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
