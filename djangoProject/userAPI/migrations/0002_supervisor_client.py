# Generated by Django 4.2.14 on 2024-07-21 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('NB_GSM', models.CharField(max_length=100, null=True)),
                ('pseudo', models.CharField(max_length=100, null=True)),
                ('e_mail', models.EmailField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
                ('prenom', models.CharField(blank=True, max_length=100, null=True)),
                ('NB_GSM', models.CharField(max_length=100, null=True)),
                ('pseudo', models.CharField(max_length=100, null=True)),
                ('e_mail', models.EmailField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='userAPI.supervisor')),
            ],
        ),
    ]
