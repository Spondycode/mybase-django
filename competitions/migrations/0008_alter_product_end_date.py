# Generated by Django 4.1 on 2023-09-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0007_remove_product_owner_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(),
        ),
    ]