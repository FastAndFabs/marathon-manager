# Generated by Django 5.0.6 on 2024-05-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("runs", "0007_run_trigger_warning"),
    ]

    operations = [
        migrations.AlterField(
            model_name="run",
            name="runners",
            field=models.ManyToManyField(null=True, related_name="runs", to="runs.person"),
        ),
    ]
