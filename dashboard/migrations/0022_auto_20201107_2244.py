# Generated by Django 3.1.3 on 2020-11-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_buybid_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immaturecoins',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
