# Generated by Django 2.2 on 2022-11-05 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(blank=True, max_length=30, unique=True)),
                ('email', models.CharField(default='', max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
