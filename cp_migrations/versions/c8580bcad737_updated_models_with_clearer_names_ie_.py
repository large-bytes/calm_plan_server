"""updated models with clearer names IE Tasks to Task

Revision ID: c8580bcad737
Revises: fe710a9ef054
Create Date: 2025-04-18 17:23:37.453297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8580bcad737'
down_revision: Union[str, None] = 'fe710a9ef054'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
