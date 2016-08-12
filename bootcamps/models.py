from __future__ import unicode_literals

from django.db import models

# Abstract Base Class : ContextForm
class ContextForm(models.Model):
	title = models.CharField(max_length=255)
	contents = models.TextField(null=True)
	date_created = models.DateField(auto_now_add=True, blank=True)

	class Meta:
		abstract = True

# Inherits from ContextForm
class Bootcamp(ContextForm):
	date_to_begin = models.DateField(null=True)
	date_to_end   = models.DateField(null=True)

	# including instructor
	participants = models.ManyToManyField('accounts.CustomUser', through='bootcamps.BootcampUserRegistration')
	precourses = models.ManyToManyField('bootcamps.Precourse', through='bootcamps.BootcampPrecourseRegistration')

	place_taken = models.CharField(max_length=255)
	register_cost = models.IntegerField()

	def __str__(self);
		return self.title

# Inherits from ContextForm
class Precourse(ContextForm):
	chapters = models.ManyToManyField('bootcamps.Chapter', through='bootcamps.PrecourseChapterRegistration')

	def __str__(self):
		return self.title

### Precourse has many chapters ###
# Inherits from ContextForm
class Chapter(ContextForm):
	correct_users 	= models.ManyToManyField('accounts.User')

	def __str__(self):
		return self.title

class BootcampUserRegistration(models.Model):
	bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE)
	# when creating a user, "grade" attribute should be specified to differentiate between normal users and instructors
	user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
	date_registered = models.DateField(auto_now_add=True, blank=True)

class 
