# Generated by Django 2.2.3 on 2019-08-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp2', '0002_auto_20190805_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='num',
            field=models.IntegerField(),
        ),
    ]
