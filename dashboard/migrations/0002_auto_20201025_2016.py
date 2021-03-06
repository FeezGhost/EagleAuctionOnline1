# Generated by Django 3.1.2 on 2020-10-25 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('bided', models.IntegerField(default=0)),
                ('remaining', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bided', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ManyToManyField(to='dashboard.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('bids', models.ManyToManyField(to='dashboard.Bids')),
                ('customer', models.ManyToManyField(to='dashboard.Customer')),
            ],
        ),
    ]
