# Generated by Django 4.1.7 on 2023-05-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('agent', 'Agent'), ('manager', 'Manager')], default='agent', max_length=20),
        ),
    ]
