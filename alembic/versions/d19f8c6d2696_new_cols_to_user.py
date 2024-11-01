"""new cols to User

Revision ID: d19f8c6d2696
Revises: e9128cde6b8a
Create Date: 2024-11-01 15:27:14.692917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd19f8c6d2696'
down_revision: Union[str, None] = 'e9128cde6b8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone', sa.String(length=20), nullable=False))
    op.add_column('users', sa.Column('comorbidities', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('medicines', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('allergies', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('objectives', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'objectives')
    op.drop_column('users', 'allergies')
    op.drop_column('users', 'medicines')
    op.drop_column('users', 'comorbidities')
    op.drop_column('users', 'phone')
    # ### end Alembic commands ###
