# Generated by Django 4.1.13 on 2024-01-11 02:41
from __future__ import annotations

from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0018_alter_generalpage_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="organizers",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="event",
            name="rsvped_members",
            field=models.ManyToManyField(
                blank=True, related_name="rsvp_events", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="speakers",
            field=models.ManyToManyField(
                blank=True, related_name="speaker_events", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
