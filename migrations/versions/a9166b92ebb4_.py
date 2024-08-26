"""empty message

Revision ID: a9166b92ebb4
Revises: 1a4e8381998e
Create Date: 2024-08-26 13:55:55.679626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9166b92ebb4'
down_revision = '1a4e8381998e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.create_index('ix_excel_id', ['excel_id'], unique=False)

    with op.batch_alter_table('hl_tr_data_detail', schema=None) as batch_op:
        batch_op.alter_column('updated_by',
               existing_type=sa.UUID(),
               nullable=True)
        batch_op.create_index('ix_efficiency_transaction_id', ['efficiency_transaction_id'], unique=False)
        batch_op.create_index('ix_variable_id', ['variable_id'], unique=False)
        batch_op.create_index('ix_variable_id_efficiency_transaction_id', ['variable_id', 'efficiency_transaction_id'], unique=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('users_name_email_username_idx', ['name', 'email', 'username'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('users_name_email_username_idx')

    with op.batch_alter_table('hl_tr_data_detail', schema=None) as batch_op:
        batch_op.drop_index('ix_variable_id_efficiency_transaction_id')
        batch_op.drop_index('ix_variable_id')
        batch_op.drop_index('ix_efficiency_transaction_id')
        batch_op.alter_column('updated_by',
               existing_type=sa.UUID(),
               nullable=False)

    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.drop_index('ix_excel_id')

    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.drop_index('ix_excel_id')

    # ### end Alembic commands ###
