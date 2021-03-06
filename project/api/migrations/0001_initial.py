# Generated by Django 3.1.4 on 2021-01-06 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather', models.CharField(max_length=156)),
                ('description', models.CharField(max_length=156)),
                ('icon', models.CharField(max_length=24)),
                ('temperature', models.CharField(max_length=24)),
                ('feels_like', models.CharField(max_length=24)),
                ('temp_min', models.CharField(max_length=24)),
                ('temp_max', models.CharField(max_length=24)),
                ('humidity', models.CharField(max_length=24)),
                ('country', models.CharField(max_length=156)),
                ('name', models.CharField(max_length=156)),
            ],
        ),
    ]
