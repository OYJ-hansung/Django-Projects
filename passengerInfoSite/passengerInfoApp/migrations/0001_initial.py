# Generated by Django 4.0.3 on 2022-04-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=35)),
                ('rewardPoints', models.FloatField()),
            ],
        ),
    ]
