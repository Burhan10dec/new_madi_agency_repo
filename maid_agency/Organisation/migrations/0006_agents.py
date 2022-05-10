# Generated by Django 4.0.2 on 2022-03-20 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Organisation', '0005_alter_office_hours_friday_end_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(blank=True, max_length=50)),
                ('Photo', models.ImageField(null=True, upload_to='')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('uen', models.PositiveIntegerField(null=True)),
                ('NRIC', models.CharField(max_length=20)),
                ('agent_registration', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('agent_type', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_person_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_person_number', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('agency_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]