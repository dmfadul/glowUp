"""added log

Revision ID: a87ed0052cae
Revises: acd97806be64
Create Date: 2024-11-08 15:55:22.805023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a87ed0052cae'
down_revision: Union[str, None] = 'acd97806be64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
