# Generated by Django 5.0.1 on 2024-01-27 03:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugapp', '0002_alter_complaint_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaintTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
