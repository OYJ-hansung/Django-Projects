# Generated by Django 4.0.3 on 2022-04-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieInfoApp', '0003_alter_movie_name_alter_movie_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='releaseDate',
            field=models.DateField(),
        ),
    ]
