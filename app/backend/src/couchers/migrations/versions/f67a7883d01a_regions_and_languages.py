"""Regions and languages

Revision ID: f67a7883d01a
Revises: 2d656b6ad999
Create Date: 2021-04-02 17:33:57.574539

"""
import geoalchemy2
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f67a7883d01a"
down_revision = "2d656b6ad999"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "language_abilities",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("language_code", sa.String(length=3), nullable=False),
        sa.Column(
            "fluency",
            sa.Enum("say_hello", "beginner", "intermediate", "advanced", "fluent", "native", name="languagefluency"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("fk_language_abilities_user_id_users")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_language_abilities")),
        sa.UniqueConstraint("user_id", "language_code", name=op.f("uq_language_abilities_user_id")),
    )
    op.create_index(op.f("ix_language_abilities_user_id"), "language_abilities", ["user_id"], unique=False)
    op.create_table(
        "regions_lived",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("region_code", sa.String(length=3), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("fk_regions_lived_user_id_users")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_regions_lived")),
        sa.UniqueConstraint("user_id", "region_code", name=op.f("uq_regions_lived_user_id")),
    )
    op.create_index(op.f("ix_regions_lived_user_id"), "regions_lived", ["user_id"], unique=False)
    op.create_table(
        "regions_visited",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("region_code", sa.String(length=3), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("fk_regions_visited_user_id_users")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_regions_visited")),
        sa.UniqueConstraint("user_id", "region_code", name=op.f("uq_regions_visited_user_id")),
    )
    op.create_index(op.f("ix_regions_visited_user_id"), "regions_visited", ["user_id"], unique=False)
    op.drop_column("users", "languages")
    op.drop_column("users", "countries_visited")
    op.drop_column("users", "countries_lived")


def downgrade():
    op.add_column("users", sa.Column("countries_lived", sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column("users", sa.Column("countries_visited", sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column("users", sa.Column("languages", sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f("ix_regions_visited_user_id"), table_name="regions_visited")
    op.drop_table("regions_visited")
    op.drop_index(op.f("ix_regions_lived_user_id"), table_name="regions_lived")
    op.drop_table("regions_lived")
    op.drop_index(op.f("ix_language_abilities_user_id"), table_name="language_abilities")
    op.drop_table("language_abilities")
