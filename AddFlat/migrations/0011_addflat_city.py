# Generated by Django 4.1.6 on 2023-05-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddFlat', '0010_usermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='addflat',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
