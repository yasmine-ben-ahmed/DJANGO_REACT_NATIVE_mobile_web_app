# Generated by Django 4.2.14 on 2024-07-21 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAPI', '0002_supervisor_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='user',
        ),
        migrations.DeleteModel(
            name='client',
        ),
        migrations.DeleteModel(
            name='supervisor',
        ),
    ]
