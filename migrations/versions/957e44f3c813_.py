"""empty message

Revision ID: 957e44f3c813
Revises: 80d5ef05dd3a
Create Date: 2020-08-07 15:56:14.001814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '957e44f3c813'
down_revision = '80d5ef05dd3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('cartridge_color', sa.String(length=64), nullable=True))
    op.add_column('event', sa.Column('printer_name', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_event_cartridge_color'), 'event', ['cartridge_color'], unique=False)
    op.create_index(op.f('ix_event_printer_name'), 'event', ['printer_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_printer_name'), table_name='event')
    op.drop_index(op.f('ix_event_cartridge_color'), table_name='event')
    op.drop_column('event', 'printer_name')
    op.drop_column('event', 'cartridge_color')
    # ### end Alembic commands ###
