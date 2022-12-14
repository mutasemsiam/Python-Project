# Generated by Django 2.2.4 on 2022-10-10 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('national_id', models.IntegerField()),
                ('desc', models.TextField()),
                ('role', models.CharField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('national_id', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('desc', models.TextField()),
                ('date_of_bith', models.DateField()),
                ('last_visit_date', models.DateField()),
                ('allergies', models.TextField(null=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic', to='dexterapp.Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('method', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('doctor_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_payment', to='dexterapp.Doctor')),
                ('patient_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_payment', to='dexterapp.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='clinic',
            name='doctor_clinc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='dexterapp.Doctor'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('doctor_appoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appoint', to='dexterapp.Doctor')),
                ('patient_appoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_appoint', to='dexterapp.Patient')),
            ],
        ),
    ]
