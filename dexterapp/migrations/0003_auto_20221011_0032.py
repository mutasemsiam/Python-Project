# Generated by Django 2.2.4 on 2022-10-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dexterapp', '0002_appointment_national_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date_of_bith',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_visit_date',
            field=models.DateField(null=True),
        ),
    ]
