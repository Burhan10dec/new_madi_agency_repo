# Generated by Django 4.0.2 on 2022-04-11 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0044_alter_staff_emp_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='staff',
            new_name='Agency_staff',
        ),
    ]
