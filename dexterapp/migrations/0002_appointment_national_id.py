# Generated by Django 2.2.4 on 2022-10-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dexterapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='national_id',
            field=models.IntegerField(default=None),
        ),
    ]
