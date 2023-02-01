# Generated by Django 4.1.5 on 2023-02-01 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("message", models.TextField()),
                ("delivery_date", models.DateField()),
                (
                    "notification_status",
                    models.CharField(
                        choices=[("unread", "UNREAD"), ("read", "READ")],
                        default="unread",
                        max_length=20,
                    ),
                ),
                (
                    "notification_type",
                    models.CharField(
                        choices=[
                            ("urgent", "URGENT"),
                            ("notice", "NOTICE"),
                            ("warning", "WARNING"),
                        ],
                        default="notice",
                        max_length=20,
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
        ),
        migrations.CreateModel(
            name="EcomProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=80)),
                ("building_number", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
