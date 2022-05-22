# Generated by Django 4.0.4 on 2022-05-21 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0010_alter_additionalinfo_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(2, 'comedy'), (0, 'other'), (1, 'drama'), (3, 'sci-fi')], default=0),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(blank=True, max_length=5, null=True)),
                ('review', models.TextField(blank=True, default='')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmy.film')),
            ],
        ),
    ]