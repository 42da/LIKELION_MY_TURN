# Generated by Django 2.2.3 on 2019-08-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='num',
            field=models.CharField(max_length=200),
        ),
    ]
