from django.db import models
from django.contrib.auth.models import AbstractUser

def get_upload_path(instance, filename):
    return "avatars/{0}/{1}".format(instance, filename)

class User(AbstractUser):
    avatar = models.ImageField(upload_to=get_upload_path)
    
    def __str__(self):
        return f"{self.username}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, null=True, blank=True, default='Kenya')
    
    def __str__(self):
        return f"{self.user.username}"