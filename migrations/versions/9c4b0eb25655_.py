"""empty message

Revision ID: 9c4b0eb25655
Revises: e24b5630a12c
Create Date: 2023-06-15 22:43:01.985698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c4b0eb25655'
down_revision = 'e24b5630a12c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journal_entries',
    sa.Column('entry_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('mood', sa.String(length=255), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('entry_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journal_entries')
    # ### end Alembic commands ###