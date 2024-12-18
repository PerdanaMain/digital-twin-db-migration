"""empty message

Revision ID: f090b2fc9226
Revises: 5a6c58c6a4aa
Create Date: 2024-10-29 16:17:24.848413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f090b2fc9226'
down_revision = '5a6c58c6a4aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dl_wo_staging', schema=None) as batch_op:
        batch_op.add_column(sa.Column('downtime', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dl_wo_staging', schema=None) as batch_op:
        batch_op.drop_column('downtime')

    # ### end Alembic commands ###
