# Generated by Django 4.0.2 on 2022-03-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0015_willingness_rest_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdws',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mdws',
            name='education',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mdws',
            name='martial_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mdws',
            name='religion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mdws',
            name='spoken_language',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]