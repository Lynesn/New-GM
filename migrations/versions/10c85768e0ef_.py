"""empty message

Revision ID: 10c85768e0ef
Revises: 56d1409ee7ab
Create Date: 2019-12-02 13:54:54.967934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10c85768e0ef'
down_revision = '56d1409ee7ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('date_created', table_name='packages')
    op.drop_index('date_to_deliver', table_name='packages')
    op.drop_index('name', table_name='packages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'packages', ['name'], unique=True)
    op.create_index('date_to_deliver', 'packages', ['date_to_deliver'], unique=True)
    op.create_index('date_created', 'packages', ['date_created'], unique=True)
    # ### end Alembic commands ###
