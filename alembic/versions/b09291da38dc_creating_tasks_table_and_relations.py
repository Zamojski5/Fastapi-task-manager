"""creating tasks table and relations

Revision ID: b09291da38dc
Revises: f36aa865f320
Create Date: 2024-06-27 23:23:36.438747

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import ENUM
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b09291da38dc'
down_revision: Union[str, None] = 'f36aa865f320'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Tworzenie enum typu dla kolumny status
    status_enum = sa.Enum('to_do', 'in_progress', 'done', name='status_enum')
    status_enum.create(op.get_bind(), checkfirst=True)

    # Dodawanie kolumn do istniejącej tabeli tasks
    op.add_column('tasks', sa.Column('name', sa.String, nullable=False))
    op.add_column('tasks', sa.Column('content', sa.String, nullable=False))
    op.add_column('tasks', sa.Column('status', status_enum, nullable=False, server_default='to_do'))
    op.add_column('tasks', sa.Column('description', sa.String, nullable=True))
    op.add_column('tasks', sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False))

def downgrade() -> None:
    # Usuwanie kolumn z istniejącej tabeli tasks
    op.drop_column('tasks', 'name')
    op.drop_column('tasks', 'content')
    op.drop_column('tasks', 'status')
    op.drop_column('tasks', 'description')
    op.drop_column('tasks', 'owner_id')

    # Usuwanie enum typu dla kolumny status
    status_enum = sa.Enum('to_do', 'in_progress', 'done', name='status_enum')
    status_enum.drop(op.get_bind(), checkfirst=True)