"""add exceptions_count field to WorkflowRun model

Revision ID: cf8f4fc45278
Revises: 01d6889832f7
Create Date: 2024-11-28 05:53:21.576178

"""
from alembic import op
import models as models
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf8f4fc45278'
down_revision = '01d6889832f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workflow_runs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('exceptions_count', sa.Integer(), server_default=sa.text('0'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workflow_runs', schema=None) as batch_op:
        batch_op.drop_column('exceptions_count')

    # ### end Alembic commands ###
