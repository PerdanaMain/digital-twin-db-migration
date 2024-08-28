"""empty message

Revision ID: 0b8a366fe546
Revises: 70d9ec8e81f6
Create Date: 2024-08-27 11:28:33.017200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b8a366fe546'
down_revision = '70d9ec8e81f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hl_ms_excel_variables_cause',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('parent_id', sa.UUID(), nullable=True, comment='ref to id table ini sendiri (recursive)'),
    sa.Column('variable_id', sa.UUID(), nullable=False),
    sa.Column('nama', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=100), nullable=True),
    sa.Column('updated_by', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['hl_ms_excel_variables_cause.id'], ),
    sa.ForeignKeyConstraint(['variable_id'], ['hl_ms_excel_variables.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hl_ms_excel_variables_header',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('variable_id', sa.UUID(), nullable=False),
    sa.Column('nama', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=100), nullable=True),
    sa.Column('updated_by', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['variable_id'], ['hl_ms_excel_variables.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hl_tr_data_detail_root_cause',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('data_detail_id', sa.UUID(), nullable=True, comment='Ref to hl_tr_data_detail'),
    sa.Column('cause_id', sa.UUID(), nullable=True, comment='Ref to hl_m_cause 1 to many'),
    sa.Column('is_repair', sa.Boolean(), nullable=True, comment='1=ya, 0=tidak'),
    sa.Column('biaya', sa.Float(), nullable=True, comment='Besar Biaya yang dikeluarkan (input)'),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.UUID(), nullable=True),
    sa.Column('updated_by', sa.UUID(), nullable=True),
    sa.Column('variable_header_value', sa.JSON(), nullable=True, comment="[{id: 9, nama: 'sdasdas asdasd', val: 1}]"),
    sa.ForeignKeyConstraint(['cause_id'], ['hl_ms_excel_variables_cause.id'], ),
    sa.ForeignKeyConstraint(['data_detail_id'], ['hl_tr_data_detail.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.add_column(sa.Column('excel_variable_name', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('is_pareto', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('is_faktor_koreksi', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('is_nilai_losses', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.drop_column('is_nilai_losses')
        batch_op.drop_column('is_faktor_koreksi')
        batch_op.drop_column('is_pareto')
        batch_op.drop_column('excel_variable_name')

    op.drop_table('hl_tr_data_detail_root_cause')
    op.drop_table('hl_ms_excel_variables_header')
    op.drop_table('hl_ms_excel_variables_cause')
    # ### end Alembic commands ###