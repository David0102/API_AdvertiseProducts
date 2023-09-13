"""att nullable products

Revision ID: 4a63b1be76c9
Revises: 2a819e9a16e5
Create Date: 2023-09-13 01:57:31.216979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a63b1be76c9'
down_revision: Union[str, None] = '2a819e9a16e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
