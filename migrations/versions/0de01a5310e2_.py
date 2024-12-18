"""empty message

Revision ID: 0de01a5310e2
Revises: 1d7d9e8ece17
Create Date: 2024-10-23 14:49:55.445336

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0de01a5310e2"
down_revision = "1d7d9e8ece17"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("dl_psd_value", schema=None) as batch_op:
        batch_op.add_column(sa.Column("psd_value", sa.Float(), nullable=True))
        batch_op.add_column(sa.Column("total_value_1", sa.Float(), nullable=True))
        batch_op.add_column(sa.Column("total_value_2", sa.Float(), nullable=True))
        batch_op.add_column(sa.Column("total_value_3", sa.Float(), nullable=True))
        batch_op.add_column(sa.Column("max_value_1", sa.Float(), nullable=True))
        batch_op.add_column(sa.Column("max_value_2", sa.Float(), nullable=True))
        batch_op.add_column(sa.Column("max_value_3", sa.Float(), nullable=True))
        batch_op.drop_column("value")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("dl_psd_value", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "value", sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False
            )
        )
        batch_op.drop_column("max_value_3")
        batch_op.drop_column("max_value_2")
        batch_op.drop_column("max_value_1")
        batch_op.drop_column("total_value_3")
        batch_op.drop_column("total_value_2")
        batch_op.drop_column("total_value_1")
        batch_op.drop_column("psd_value")

    # ### end Alembic commands ###
