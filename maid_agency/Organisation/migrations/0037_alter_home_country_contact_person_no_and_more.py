# Generated by Django 4.0.2 on 2022-04-03 10:11

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0036_alter_agents_company_contact_person_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_country',
            name='contact_person_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='home_country',
            name='contact_person_no_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
