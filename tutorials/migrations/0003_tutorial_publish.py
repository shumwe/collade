# Generated by Django 4.1 on 2022-08-31 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0002_alter_tutorial_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="tutorial",
            name="publish",
            field=models.BooleanField(default=True),
        ),
    ]
