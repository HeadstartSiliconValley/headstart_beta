from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20)
	grade = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username
