"""att user_id by products

Revision ID: d581aab5575d
Revises: 5aa9d34b8261
Create Date: 2023-09-13 00:21:40.359778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd581aab5575d'
down_revision: Union[str, None] = '5aa9d34b8261'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
