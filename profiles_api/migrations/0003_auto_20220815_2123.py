# Generated by Django 2.2 on 2022-08-15 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='created_on',
            new_name='created_at',
        ),
    ]
