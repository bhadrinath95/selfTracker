# Generated by Django 3.1.5 on 2021-01-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycletracker',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
