# Generated by Django 4.0.2 on 2022-04-12 05:25

import Organisation.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0047_alter_agency_staff_nric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('doc', models.FileField(blank=True, null=True, upload_to=Organisation.models.Staff_document_path_and_rename)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Organisation.agency_staff')),
            ],
        ),
    ]