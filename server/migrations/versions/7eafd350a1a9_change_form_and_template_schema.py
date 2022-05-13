"""change form and template schema

Revision ID: 7eafd350a1a9
Revises: 5423f554155e
Create Date: 2022-03-10 13:46:37.664434

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "7eafd350a1a9"
down_revision = "5423f554155e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("form", sa.Column("formTemplateId", sa.Integer(), nullable=False))
    op.alter_column(
        "form",
        "lastEditedBy",
        existing_type=mysql.INTEGER(display_width=11),
        nullable=False,
    )
    op.create_foreign_key(
        "fk_form_form_template_form_template_id_id",
        "form",
        "form_template",
        ["formTemplateId"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_form_user_last_edited_by_id",
        "form",
        "user",
        ["lastEditedBy"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_column("form", "createdBy")
    op.drop_column("form_template", "lastEditedBy")
    op.drop_column("form_template", "createdBy")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "form_template",
        sa.Column(
            "createdBy",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "form_template",
        sa.Column(
            "lastEditedBy",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "form",
        sa.Column(
            "createdBy",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_constraint(
        "fk_form_form_template_form_template_id_id", "form", type_="foreignkey"
    )
    op.drop_constraint("fk_form_user_last_edited_by_id", "form", type_="foreignkey")
    op.alter_column(
        "form",
        "lastEditedBy",
        existing_type=mysql.INTEGER(display_width=11),
        nullable=True,
    )
    op.drop_column("form", "formTemplateId")
    # ### end Alembic commands ###