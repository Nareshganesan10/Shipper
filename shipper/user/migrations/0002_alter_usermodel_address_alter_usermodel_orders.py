# Generated by Django 5.0.3 on 2024-03-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='orders',
            field=models.TextField(null=True),
        ),
    ]
