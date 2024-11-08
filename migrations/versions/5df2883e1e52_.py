"""empty message

Revision ID: 5df2883e1e52
Revises: 0d1316045668
Create Date: 2024-10-17 09:52:08.036437

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5df2883e1e52'
down_revision = '0d1316045668'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dl_fft_value',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('tag_id', sa.BigInteger(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['dl_ms_tag.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('dl_fft_fetch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dl_fft_fetch',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('tag_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('time_stamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('value', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('units_abbreviation', sa.VARCHAR(length=15), autoincrement=False, nullable=False),
    sa.Column('good', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('questionable', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('substituted', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('annotated', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['dl_ms_tag.id'], name='dl_fft_fetch_tag_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='dl_fft_fetch_pkey')
    )
    op.drop_table('dl_fft_value')
    # ### end Alembic commands ###
