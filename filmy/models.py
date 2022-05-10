from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    desc = models.TextField(default='Bardzo ciekawy film o miłości.')
    rating_imdb = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)

    def __str__(self):
        return self.title_and_date()

    def title_and_date(self):
        return f'{self.title} ({self.year})'
