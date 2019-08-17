# Generated by Django 2.1 on 2019-08-15 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('joined_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
