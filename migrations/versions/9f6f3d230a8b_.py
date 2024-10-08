"""empty message

Revision ID: 9f6f3d230a8b
Revises: 4a459a41bad5
Create Date: 2024-09-12 13:51:12.373836

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9f6f3d230a8b'
down_revision = '4a459a41bad5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.alter_column('sequence',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=300),
               nullable=False)

    with op.batch_alter_table('hl_tr_data_detail_root_cause', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_tr_data_detail_root_cause', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)

    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=300),
               nullable=True)
        batch_op.alter_column('sequence',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
