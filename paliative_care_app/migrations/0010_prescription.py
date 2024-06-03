# Generated by Django 5.0.3 on 2024-05-28 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paliative_care_app', '0009_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.FileField(upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paliative_care_app.patient')),
            ],
        ),
    ]