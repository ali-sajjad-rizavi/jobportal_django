from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Jobpost(models.Model):
    JOB_CATEGORIES = [
        ('other', 'Other'),
        ('it', 'IT and Software'),
        ('data_entry', 'Data Entry'),
        ('graphic_design', 'Graphic Design'),
        ('teaching', 'Teaching'),
        ('home_tuiton', 'Home Tuition'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=JOB_CATEGORIES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobpost', kwargs={'pk': self.pk})
