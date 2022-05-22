# Generated by Django 4.0.4 on 2022-05-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0011_alter_additionalinfo_genre_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(0, 'other'), (3, 'sci-fi'), (2, 'comedy'), (1, 'drama')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]