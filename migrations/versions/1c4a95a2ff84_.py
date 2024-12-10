"""empty message

Revision ID: 1c4a95a2ff84
Revises: 
Create Date: 2024-12-05 16:22:09.224780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c4a95a2ff84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hubspot_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lead',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('adviser_name', sa.String(length=255), nullable=True),
    sa.Column('lead_name', sa.String(length=255), nullable=True),
    sa.Column('linkedin_url', sa.String(length=255), nullable=True),
    sa.Column('lead_title', sa.String(length=255), nullable=True),
    sa.Column('company_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('lead')
    op.drop_table('hubspot_token')
    # ### end Alembic commands ###