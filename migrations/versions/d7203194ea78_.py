"""empty message

Revision ID: d7203194ea78
Revises: f090b2fc9226
Create Date: 2024-10-29 16:20:34.640793

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd7203194ea78'
down_revision = 'f090b2fc9226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dl_wo_staging', schema=None) as batch_op:
        batch_op.alter_column('assetnum',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dl_wo_staging', schema=None) as batch_op:
        batch_op.alter_column('assetnum',
               existing_type=sa.Text(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)

    # ### end Alembic commands ###