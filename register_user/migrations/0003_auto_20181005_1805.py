# Generated by Django 2.1.2 on 2018-10-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_user', '0002_auto_20181005_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
