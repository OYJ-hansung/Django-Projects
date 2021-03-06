# Generated by Django 4.0.3 on 2022-04-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieInfoApp', '0002_movie_name_movie_releasedate_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='releaseDate',
            field=models.DateField(null=True),
        ),
    ]
