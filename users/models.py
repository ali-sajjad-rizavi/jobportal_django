from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField()
    image = models.ImageField(default='profile-picture.jpg', upload_to='profile-images')

    def __str__(self):
        return f'{self.user.username} Profile'
