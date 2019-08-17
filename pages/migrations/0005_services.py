# Generated by Django 2.1 on 2019-08-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]
