# Generated by Django 4.1.5 on 2023-02-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecom_store", "0004_remove_store_store_id_store_store_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="store_code",
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_name",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
