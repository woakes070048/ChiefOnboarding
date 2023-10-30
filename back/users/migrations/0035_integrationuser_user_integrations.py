# Generated by Django 4.2.6 on 2023-10-24 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0022_alter_integration_manifest_and_more"),
        ("users", "0034_alter_user_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="IntegrationUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("revoked", models.BooleanField(default=False)),
                (
                    "integration",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="integrations.integration",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "integration")},
            },
        ),
        migrations.AddField(
            model_name="user",
            name="integrations",
            field=models.ManyToManyField(
                related_name="user_integrations",
                through="users.IntegrationUser",
                to="integrations.integration",
            ),
        ),
    ]