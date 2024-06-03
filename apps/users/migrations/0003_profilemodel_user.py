# Generated by Django 5.0.6 on 2024-06-02 11:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
