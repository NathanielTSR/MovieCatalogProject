# Generated by Django 2.1.3 on 2018-11-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvdmovie', '0004_auto_20181126_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='diskcondition',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]