# Generated by Django 4.0.2 on 2022-03-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0009_mdws'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]