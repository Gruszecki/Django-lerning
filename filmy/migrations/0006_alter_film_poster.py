# Generated by Django 4.0.4 on 2022-05-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0005_alter_film_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, default='/posters/default.jpg', upload_to='posters'),
        ),
    ]
