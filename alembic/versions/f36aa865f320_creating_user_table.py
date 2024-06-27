"""creating user table

Revision ID: f36aa865f320
Revises: c0e42ce8e4dc
Create Date: 2024-06-27 23:01:50.262867

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import TIMESTAMP
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f36aa865f320'
down_revision: Union[str, None] = 'c0e42ce8e4dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        
    )

def downgrade() -> None:
    op.drop_table('users')