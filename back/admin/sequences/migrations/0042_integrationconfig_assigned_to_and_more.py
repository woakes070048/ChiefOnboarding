# Generated by Django 4.2.6 on 2023-10-29 01:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sequences", "0041_condition_condition_admin_tasks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="integrationconfig",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned_user_integration",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Pick user",
            ),
        ),
        migrations.AddField(
            model_name="integrationconfig",
            name="person_type",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Manager"), (2, "Buddy"), (3, "Custom")],
                help_text=(
                    "Leave empty to automatically check the integration as "
                    "created/removed."
                ),
                null=True,
                verbose_name="Assigned to",
            ),
        ),
        migrations.AddField(
            model_name="sequence",
            name="category",
            field=models.IntegerField(
                choices=[(0, "Onboarding sequence"), (1, "Offboarding sequence")],
                default=0,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="condition",
            name="days",
            field=models.IntegerField(
                default=1, verbose_name="Amount of days before/after"
            ),
        ),
    ]