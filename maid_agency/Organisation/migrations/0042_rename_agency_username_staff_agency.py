# Generated by Django 4.0.2 on 2022-04-10 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0041_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='agency_username',
            new_name='agency',
        ),
    ]
