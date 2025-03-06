# Generated by Django 5.1.6 on 2025-03-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='profilePic',
            field=models.ImageField(blank=True, default='images/logo1', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='userPic',
            field=models.ImageField(blank=True, default='images/propic.jpeg', null=True, upload_to=''),
        ),
    ]
