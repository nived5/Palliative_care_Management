# Generated by Django 5.0.3 on 2024-05-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paliative_care_app', '0005_doctor_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_schedule',
            name='Doctor_Name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
