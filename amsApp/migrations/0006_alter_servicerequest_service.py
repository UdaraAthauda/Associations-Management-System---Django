# Generated by Django 5.1.6 on 2025-03-09 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amsApp', '0005_service_servicerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='amsApp.service', unique=True),
        ),
    ]
