"""att user_id by products

Revision ID: 2a819e9a16e5
Revises: d581aab5575d
Create Date: 2023-09-13 00:24:38.904538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a819e9a16e5'
down_revision: Union[str, None] = 'd581aab5575d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
