"""ajout des colonnes jeu bridge

Revision ID: e0a569c2d5be
Revises: 
Create Date: 2026-04-16 06:44:06.363706

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e0a569c2d5be'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # On ajoute uniquement les colonnes qui n'existent pas encore sur Neon
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chances_bridge', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('derniere_maj_chances', sa.Date(), nullable=True))

def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('derniere_maj_chances')
        batch_op.drop_column('chances_bridge')

