# Generated by Django 3.0.7 on 2020-07-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='+91 ', max_length=14),
        ),
    ]
