# Generated by Django 4.0.2 on 2022-03-29 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0023_remove_agents_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdws',
            name='agent_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Organisation.agents'),
        ),
    ]
