# Generated by Django 4.2 on 2023-09-29 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("add_teammate", "0002_alter_team_joined_date"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="team",
            new_name="Person",
        ),
    ]
