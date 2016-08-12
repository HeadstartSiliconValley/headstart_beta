from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)    
    grade = models.IntegerField()
    photo = models.ImageField(upload_to = 'pic_folder/')