# Generated by Django 4.1.7 on 2023-02-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_store', '0010_storeproduct_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproduct',
            name='product_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]