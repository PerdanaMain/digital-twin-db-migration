"""empty message

Revision ID: 7d79783df4cc
Revises: 23d30a1414d1
Create Date: 2024-08-20 11:01:52.760075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d79783df4cc'
down_revision = '23d30a1414d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('case_inputs', schema=None) as batch_op:
        batch_op.drop_constraint('case_inputs_cases_id_key', type_='unique')
        batch_op.drop_constraint('case_inputs_variables_id_key', type_='unique')

    with op.batch_alter_table('case_outputs', schema=None) as batch_op:
        batch_op.drop_constraint('case_outputs_cases_id_key', type_='unique')
        batch_op.drop_constraint('case_outputs_variables_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('case_outputs', schema=None) as batch_op:
        batch_op.create_unique_constraint('case_outputs_variables_id_key', ['variables_id'])
        batch_op.create_unique_constraint('case_outputs_cases_id_key', ['cases_id'])

    with op.batch_alter_table('case_inputs', schema=None) as batch_op:
        batch_op.create_unique_constraint('case_inputs_variables_id_key', ['variables_id'])
        batch_op.create_unique_constraint('case_inputs_cases_id_key', ['cases_id'])

    # ### end Alembic commands ###
