# Generated by Django 5.0.2 on 2024-02-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
