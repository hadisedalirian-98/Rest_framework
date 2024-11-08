# Generated by Django 5.1.3 on 2024-11-08 08:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2024, 11, 8, 8, 28, 33, 562231, tzinfo=datetime.timezone.utc))),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='task.category')),
            ],
        ),
    ]