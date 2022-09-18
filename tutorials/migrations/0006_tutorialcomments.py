# Generated by Django 4.1 on 2022-09-18 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tutorials", "0005_alter_favourite_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="TutorialComments",
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
                ("message", models.TextField(max_length=100)),
                ("display", models.BooleanField(default=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tutorials.tutorialcomments",
                    ),
                ),
                (
                    "parent_tutorial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
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
