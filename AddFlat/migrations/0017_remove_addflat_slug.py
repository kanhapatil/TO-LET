# Generated by Django 4.1.6 on 2023-06-11 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AddFlat', '0016_addflat_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addflat',
            name='slug',
        ),
    ]
