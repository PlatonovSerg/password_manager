# Generated by Django 5.0.6 on 2024-06-27 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='service_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='password', to='password.service'),
        ),
    ]
