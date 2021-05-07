# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-01 08:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0002_auto_20210131_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='name',
            new_name='business_name',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='image',
            new_name='hood_image',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='name',
            new_name='hood_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_image',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='population',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health_tell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhoods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
    ]