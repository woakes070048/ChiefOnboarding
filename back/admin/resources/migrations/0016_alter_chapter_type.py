# Generated by Django 3.2.16 on 2023-02-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0015_auto_20220929_0102"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="type",
            field=models.IntegerField(
                choices=[(0, "Page"), (1, "Folder"), (2, "Questions")]
            ),
        ),
    ]