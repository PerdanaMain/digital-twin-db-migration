"""empty message

Revision ID: 1cd16b00a79f
Revises: a909e1057cc7
Create Date: 2024-10-01 16:46:13.788199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1cd16b00a79f'
down_revision = 'a909e1057cc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hl_tr_thermoflow_log')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hl_tr_thermoflow_log',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('efficiency_transaction_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=300), autoincrement=False, nullable=False),
    sa.Column('error_message', sa.VARCHAR(length=300), autoincrement=False, nullable=True),
    sa.Column('completed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['efficiency_transaction_id'], ['hl_tr_data.id'], name='hl_tr_thermoflow_log_efficiency_transaction_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='hl_tr_thermoflow_log_pkey')
    )
    # ### end Alembic commands ###