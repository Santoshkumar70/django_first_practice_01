# Generated by Django 4.2.7 on 2023-11-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
            ],
        ),
    ]
