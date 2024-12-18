"""empty message

Revision ID: 661004f14640
Revises: dd2a2df18045
Create Date: 2024-10-29 09:34:31.035785

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '661004f14640'
down_revision = 'dd2a2df18045'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dl_wo_staging', schema=None) as batch_op:
        batch_op.add_column(sa.Column('actstart', sa.DateTime(), nullable=True))
        batch_op.drop_column('acstart')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dl_wo_staging', schema=None) as batch_op:
        batch_op.add_column(sa.Column('acstart', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.drop_column('actstart')

    # ### end Alembic commands ###
