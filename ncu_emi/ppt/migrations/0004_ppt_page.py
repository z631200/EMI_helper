# Generated by Django 5.1 on 2024-08-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ppt", "0003_alter_ppt_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ppt_page",
            fields=[
                (
                    "ppt_page_id",
                    models.AutoField(
                        db_column="ppt_page_id", primary_key=True, serialize=False
                    ),
                ),
                (
                    "uploaded_id",
                    models.CharField(
                        blank=True, db_column="uploaded_id", max_length=100, null=True
                    ),
                ),
            ],
            options={
                "db_table": "ppt_page",
                "managed": False,
            },
        ),
    ]
