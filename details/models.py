from __future__ import unicode_literals
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.db.models import Avg


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    pub_avg_rating = models.Aggregate(output_field=Decimal())

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    author_avg_rating = models.Aggregate(output_field=Decimal())
    maximum_book = models.IntegerField(default=0)
    minimum_book = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=150, verbose_name='Book Name')
    image = models.ImageField(null=True, blank=True, verbose_name='Book Image')
    author = models.ManyToManyField(Author)
    rating = models.DecimalField(null=True, blank=True, verbose_name='Expert Rating', max_digits=2, decimal_places=1)
    # user_rating = models.DecimalField(null=True, blank=True, verbose_name='User Rating', max_digits=2, decimal_places=1)
    pub = models.ForeignKey(Publisher)
    price = models.FloatField(validators=[MinValueValidator(0.9)], verbose_name='Book Price')
    published_date = models.DateField(blank=True, null=True, verbose_name='Date of Book published')

    def __str__(self):
        return self.name


class BookRating(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    rating = models.IntegerField(null=True, blank=True, default=None)
    book = models.ForeignKey(Book, related_name='book_rating')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)

    # def __str__(self):
    #     return self.rating
