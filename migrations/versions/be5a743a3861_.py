"""empty message

Revision ID: be5a743a3861
Revises: 0de01a5310e2
Create Date: 2024-10-28 15:43:10.646261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be5a743a3861'
down_revision = '0de01a5310e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dl_wo_staging',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('assetnum', sa.DateTime(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('unit', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=25), nullable=True),
    sa.Column('system_tag', sa.String(length=5), nullable=True),
    sa.Column('wonum', sa.String(length=10), nullable=True),
    sa.Column('worktype', sa.String(length=5), nullable=True),
    sa.Column('jpnum', sa.String(length=10), nullable=True),
    sa.Column('workgroup', sa.String(length=30), nullable=True),
    sa.Column('mat_cost_max', sa.Float(), nullable=True),
    sa.Column('serv_cost_max', sa.Float(), nullable=True),
    sa.Column('total_cost_max', sa.Float(), nullable=True),
    sa.Column('wo_start', sa.DateTime(), nullable=True),
    sa.Column('wo_finish', sa.DateTime(), nullable=True),
    sa.Column('wo_start_olah', sa.DateTime(), nullable=True),
    sa.Column('wo_finish_olah', sa.DateTime(), nullable=True),
    sa.Column('reportdate', sa.DateTime(), nullable=True),
    sa.Column('reportdate_olah', sa.DateTime(), nullable=True),
    sa.Column('time_to_event', sa.Float(), nullable=True),
    sa.Column('acstart', sa.DateTime(), nullable=True),
    sa.Column('actfinish', sa.DateTime(), nullable=True),
    sa.Column('acstart_olah', sa.DateTime(), nullable=True),
    sa.Column('actfinish_olah', sa.DateTime(), nullable=True),
    sa.Column('act_repair', sa.Float(), nullable=True),
    sa.Column('jumlah_labor', sa.Integer(), nullable=True),
    sa.Column('need_downtime', sa.String(length=100), nullable=True),
    sa.Column('validation_downtime', sa.String(length=100), nullable=True),
    sa.Column('down_0_and_not_oh', sa.Integer(), nullable=True),
    sa.Column('failure_code', sa.String(length=10), nullable=True),
    sa.Column('problem_code', sa.String(length=10), nullable=True),
    sa.Column('act_finish_wo_start', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dl_wo_staging')
    # ### end Alembic commands ###