# Generated by Django 4.1 on 2022-09-01 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tutorials", "0003_tutorial_publish"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favourite",
            fields=[
                (
                    "tutorialappbasemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="tutorials.tutorialappbasemodel",
                    ),
                ),
                (
                    "fav_tutorial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tutorials.tutorial",
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
                "ordering": ["-created"],
            },
            bases=("tutorials.tutorialappbasemodel",),
        ),
    ]
