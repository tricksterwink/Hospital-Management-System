# Generated by Django 3.2.7 on 2022-04-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0003_doctorpatientassignment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorpatientassignment',
            name='status',
            field=models.CharField(default='Open', max_length=10),
        ),
    ]
