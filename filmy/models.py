from django.db import models


class AdditionalInfo(models.Model):
    GENRE = {
        (0, 'other'),
        (1, 'drama'),
        (2, 'comedy'),
        (3, 'sci-fi'),
    }

    runtime = models.PositiveSmallIntegerField()
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE)


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    desc = models.TextField()
    rating_imdb = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=False, blank=True, default='/posters/default.jpg')
    additional_info = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.title_and_date()

    def title_and_date(self):
        return f'{self.title} ({self.year})'


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    review = models.TextField(default='', blank=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Actor(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    surname = models.CharField(max_length=64, blank=False)
    films = models.ManyToManyField(Film)
