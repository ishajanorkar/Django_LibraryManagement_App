# Generated by Django 4.1.4 on 2023-01-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickit',
            name='Aname',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tickit',
            name='cat',
            field=models.IntegerField(),
        ),
    ]
