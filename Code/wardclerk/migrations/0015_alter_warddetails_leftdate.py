# Generated by Django 4.0.1 on 2022-04-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardclerk', '0014_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warddetails',
            name='LeftDate',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
