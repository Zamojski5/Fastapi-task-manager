"""addd new column

Revision ID: bc6f7b12eab2
Revises: 24531f20db33
Create Date: 2024-06-27 22:27:14.553624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc6f7b12eab2'
down_revision: Union[str, None] = '24531f20db33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('tasks',
       sa.Column('content',sa.String(), nullable=False),



    )
    pass

def downgrade() -> None:
    op.add_column('tasks',sa.Column('content', sa.String(), nullable=False))
    pass
