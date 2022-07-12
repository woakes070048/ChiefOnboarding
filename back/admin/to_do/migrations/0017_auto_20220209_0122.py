# Generated by Django 3.2.10 on 2022-02-09 01:22

from django.db import migrations

from misc.migration_scripts.content_migrations import (
    RunPythonWithArguments,
    migrate_forms_to_wysiwyg,
)


class Migration(migrations.Migration):

    dependencies = [
        ("to_do", "0016_rename_content_json_todo_content"),
    ]

    operations = [
        RunPythonWithArguments(
            migrate_forms_to_wysiwyg,
            context={"app": "to_do", "model": "todo"},
        ),
    ]