# Generated by Django 2.1 on 2019-08-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_linking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('datetime', models.CharField(max_length=100)),
            ],
        ),
    ]
