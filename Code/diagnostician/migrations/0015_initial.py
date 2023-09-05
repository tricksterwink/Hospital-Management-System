# Generated by Django 4.0.1 on 2022-04-10 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receptionist', '0014_initial'),
        ('diagnostician', '0014_delete_diagnosis_delete_diagnostician'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostician',
            fields=[
                ('DiagnosticianID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=45)),
                ('LastName', models.CharField(max_length=45)),
                ('EmailAddress', models.CharField(max_length=45)),
                ('PermantAddress', models.CharField(default='None', max_length=100)),
                ('BloodGroup', models.CharField(max_length=45)),
                ('Salary', models.IntegerField(default=0)),
                ('Age', models.IntegerField(default=0)),
                ('Shift', models.IntegerField(default=0)),
                ('password', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('contact', models.CharField(default=None, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('DiagnosticReportID', models.IntegerField(primary_key=True, serialize=False)),
                ('labreport', models.BooleanField(default=False)),
                ('bill', models.BooleanField(default=False)),
                ('totalbill', models.IntegerField(default=0)),
                ('description', models.CharField(default=None, max_length=500)),
                ('Appointment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='receptionist.doctorpatientassignment')),
                ('Diagnostician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnostician.diagnostician')),
            ],
        ),
    ]