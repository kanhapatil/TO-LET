# Generated by Django 4.1.6 on 2023-05-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddFlat', '0002_remove_flatowner_email_remove_flatowner_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatowner',
            name='contact',
        ),
        migrations.AddField(
            model_name='flatowner',
            name='gender',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='flatowner',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='flatowner',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='flatowner',
            name='type',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
