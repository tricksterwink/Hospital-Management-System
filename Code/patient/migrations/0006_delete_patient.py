# Generated by Django 4.0.1 on 2022-04-10 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0013_delete_doctorpatientassignment_delete_receptionist'),
        ('patient', '0005_patient_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
