from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    nationality = models.CharField(max_length=50)
    camp_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'

