# Generated by Django 4.1 on 2023-09-06 19:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_ticketorder_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tickets_bought',
        ),
        migrations.RemoveField(
            model_name='ticketorder',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='char_percent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.charpercent'),
        ),
        migrations.AlterField(
            model_name='product',
            name='charity',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ticketorder',
            name='title',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
