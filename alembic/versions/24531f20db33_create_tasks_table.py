"""create tasks table

Revision ID: 24531f20db33
Revises: 
Create Date: 2024-06-27 21:55:58.717235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24531f20db33'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('tasks',
       sa.Column('id',sa.Integer(), nullable=False, primary_key=True),
       sa.Column('title', sa.String(),nullable=False),



    )
    pass


def downgrade() -> None:
    op.drop_table('tasks')
    pass
