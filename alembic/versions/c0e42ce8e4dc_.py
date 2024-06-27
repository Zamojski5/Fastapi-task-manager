"""empty message

Revision ID: c0e42ce8e4dc
Revises: bc6f7b12eab2
Create Date: 2024-06-27 22:58:54.140622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0e42ce8e4dc'
down_revision: Union[str, None] = 'bc6f7b12eab2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('tasks',
       sa.Column('id',sa.Integer(), nullable=False, primary_key=True),



    )
    pass


def downgrade() -> None:
    op.drop_table('tasks')
    pass
