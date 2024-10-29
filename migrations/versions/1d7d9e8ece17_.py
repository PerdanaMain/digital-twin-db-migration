"""empty message

Revision ID: 1d7d9e8ece17
Revises: 2bbb3c578bca
Create Date: 2024-10-17 16:40:29.502228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d7d9e8ece17'
down_revision = '2bbb3c578bca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dl_psd_value',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('tag_id', sa.BigInteger(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['dl_ms_tag.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dl_psd_value')
    # ### end Alembic commands ###