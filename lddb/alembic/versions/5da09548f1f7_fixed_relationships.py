"""fixed relationships

Revision ID: 5da09548f1f7
Revises: 82153cd99c29
Create Date: 2022-05-18 00:09:08.093162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5da09548f1f7'
down_revision = '82153cd99c29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dances', schema=None) as batch_op:
        batch_op.add_column(sa.Column('song_id', sa.String(length=36), nullable=True))
        batch_op.add_column(sa.Column('file_id', sa.String(length=36), nullable=True))
        batch_op.create_foreign_key(None, 'files', ['file_id'], ['id'])
        batch_op.create_foreign_key(None, 'songs', ['song_id'], ['id'])

    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.String(length=36), nullable=True))
        batch_op.add_column(sa.Column('file_id', sa.String(length=36), nullable=True))
        batch_op.create_foreign_key(None, 'song_authors', ['author_id'], ['id'])
        batch_op.create_foreign_key(None, 'files', ['file_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('file_id')
        batch_op.drop_column('author_id')

    with op.batch_alter_table('dances', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('file_id')
        batch_op.drop_column('song_id')

    # ### end Alembic commands ###
