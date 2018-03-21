from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Animal(models.Model):

	name            = models.CharField(max_length=120, null = False, blank = False)
	breed           = models.CharField(max_length=120, null = False, blank = False)
	age             = models.CharField(max_length=120, null = False, blank = False)
	gender          = models.CharField(max_length=120, null = False, blank = False)

	def __str__(self):
		return self.name

	