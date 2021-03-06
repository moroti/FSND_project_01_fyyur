"""empty message

Revision ID: 032244060c7b
Revises: 2eb39f6b9396
Create Date: 2020-12-29 13:18:22.562473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '032244060c7b'
down_revision = '2eb39f6b9396'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.drop_column('Artist', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
