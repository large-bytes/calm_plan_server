"""password to hashed_password, is_active to false, orm_mode to from_attributes

Revision ID: 34a964bd8924
Revises: 27357fb70167
Create Date: 2025-01-10 08:43:49.650235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34a964bd8924'
down_revision: Union[str, None] = '27357fb70167'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('disabled', sa.Boolean(), nullable=True))
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.String(length=225),
               nullable=True)
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.alter_column('users', 'hashed_password',
               existing_type=sa.String(length=225),
               type_=sa.VARCHAR(length=8),
               nullable=False)
    op.drop_column('users', 'disabled')
    # ### end Alembic commands ###
