# Generated by Django 4.0.2 on 2022-04-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0038_social_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='contact_person_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]