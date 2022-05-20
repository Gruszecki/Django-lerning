# Generated by Django 4.0.4 on 2022-05-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0007_alter_film_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runtime', models.PositiveSmallIntegerField(default=0)),
                ('genre', models.PositiveSmallIntegerField(choices=[(0, 'other'), (3, 'sci-fi'), (2, 'comedy'), (1, 'drama')], default=0)),
            ],
        ),
    ]
