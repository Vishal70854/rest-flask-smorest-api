"""empty message

Revision ID: b840b4938069
Revises: cebc4f8fd574
Create Date: 2023-05-02 20:47:09.501908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b840b4938069'
down_revision = 'cebc4f8fd574'
branch_labels = None
depends_on = None


def upgrade():
    

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint('email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('email', type_='unique')
        batch_op.drop_column('email')

    

    # ### end Alembic commands ###
