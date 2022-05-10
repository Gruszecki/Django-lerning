# Generated by Django 4.0.4 on 2022-05-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0002_film_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='desc',
            field=models.TextField(default='Bardzo ciekawy film o miłości.'),
        ),
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
        migrations.AddField(
            model_name='film',
            name='rating_imdb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]