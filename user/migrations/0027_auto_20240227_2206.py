# Generated by Django 2.2 on 2024-02-27 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_auto_20240225_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(choices=[('C', 'Crypto'), ('F', 'Futures'), ('CF', 'Cfd'), ('S', 'Stocks'), ('FX', 'Forex')], max_length=10, null=True),
        ),
    ]
