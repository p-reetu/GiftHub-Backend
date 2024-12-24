from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustUser(AbstractUser):
    age = models.PositiveIntegerField()
    gender = models.BooleanField()

class Gift(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="receiver")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="gifts/", null=True, blank=True)
    
