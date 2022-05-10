# Generated by Django 4.0.2 on 2022-04-03 10:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0033_alter_branches_mobile_number2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_person_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=12, max_length=128, region=None),
        ),
    ]
