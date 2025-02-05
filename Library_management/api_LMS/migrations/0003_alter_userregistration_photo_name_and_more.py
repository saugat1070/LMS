# Generated by Django 5.1.5 on 2025-02-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_LMS', '0002_alter_userregistration_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='photo_name',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='username',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
    ]
