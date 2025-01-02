from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_details = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
    


class Gallery(models.Model):
    title=models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True) 

class Projects(models.Model):
    title=models.CharField(max_length=255)
    image= models.ImageField(upload_to='images/', blank=True, null=True) 
    description = models.TextField()

from django.db import models

class Feedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Generates choices for ratings from 1 to 5

    name = models.CharField(max_length=100)
    comments = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)  # Use the predefined choices
    date_submitted = models.DateTimeField(auto_now_add=True)  # Fix typo in "data_submitted"

    def __str__(self):
        return f"{self.name} - {self.rating}"


    