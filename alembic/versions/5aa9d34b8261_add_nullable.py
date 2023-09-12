"""Add nullable

Revision ID: 5aa9d34b8261
Revises: 6af3f81fd8ca
Create Date: 2023-09-12 13:30:02.688722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5aa9d34b8261'
down_revision: Union[str, None] = '6af3f81fd8ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
