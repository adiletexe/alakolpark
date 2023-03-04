from django.db import models
from datetime import date

class Room(models.Model):
    pass

class Booking(models.Model):
    full_name = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    num_rooms = models.IntegerField(default=1)

class Review(models.Model):
    full_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(choices=((1, "1 star"), (2, "2 stars"), (3, "3 stars"), (4, "4 stars"), (5, "5 stars")))

    def __str__(self):
        return self.full_name

class AddModel(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    phone = models.IntegerField(max_length=14)

    def __str__(self):
        return self.name