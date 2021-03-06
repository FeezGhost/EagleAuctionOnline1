# Generated by Django 3.1.2 on 2020-10-28 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20201029_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buybid',
            name='bider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.bids'),
        ),
        migrations.AlterField(
            model_name='buybid',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')], max_length=200, null=True),
        ),
    ]
