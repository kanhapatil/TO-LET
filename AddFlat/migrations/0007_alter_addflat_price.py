# Generated by Django 4.1.6 on 2023-05-30 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddFlat', '0006_remove_addflat_flat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addflat',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
