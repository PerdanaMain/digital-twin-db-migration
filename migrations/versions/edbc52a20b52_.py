"""empty message

Revision ID: edbc52a20b52
Revises: 065da80dc3f1
Create Date: 2024-08-22 10:12:33.543735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edbc52a20b52'
down_revision = '065da80dc3f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=255), nullable=False))
        batch_op.alter_column('input_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.drop_constraint('hl_tr_data_variable_id_fkey', type_='foreignkey')
        batch_op.drop_column('variable_id')
        batch_op.drop_column('nilai')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nilai', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('variable_id', sa.UUID(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('hl_tr_data_variable_id_fkey', 'hl_ms_excel_variables', ['variable_id'], ['id'])

    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.alter_column('input_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.drop_column('category')

    # ### end Alembic commands ###
