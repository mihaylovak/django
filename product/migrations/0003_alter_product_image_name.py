# Generated by Django 4.1.6 on 2023-02-07 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_name',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]