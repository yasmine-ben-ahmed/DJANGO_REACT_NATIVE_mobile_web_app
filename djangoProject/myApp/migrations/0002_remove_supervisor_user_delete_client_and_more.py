# Generated by Django 4.2.14 on 2024-07-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
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