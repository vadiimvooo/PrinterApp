"""empty message

Revision ID: 64b6cc1820e3
Revises: 98385ec7692e
Create Date: 2020-08-04 19:24:59.622063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64b6cc1820e3'
down_revision = '98385ec7692e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('printer', sa.Column('updated_timestamp', sa.DateTime(), nullable=True))
    op.drop_index('ix_printer_creation_timestamp', table_name='printer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_printer_creation_timestamp', 'printer', ['creation_timestamp'], unique=False)
    op.drop_column('printer', 'updated_timestamp')
    # ### end Alembic commands ###
