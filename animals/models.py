from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime



User = settings.AUTH_USER_MODEL

# class Animal(models.Model):
# 	category        = models.CharField(max_length=120, null = False, blank = False)
# 	name            = models.CharField(max_length=120, null = False, blank = False)
# 	age             = models.CharField(max_length=120, null = False, blank = False)
# 	gender          = models.CharField(max_length=120, null = False, blank = False)
# 	# simage           = models.ImageField(upload_to = 'pic_folder' , blank = False)
	

# 	def __str__(self):
# 		return self.name

class Animals(models.Model):


	DOG = "dog"
	CAT = "cat"
	SNAKE = "snake"
	MALE = "male"
	FEMALE = "female"

	ANIMAL_CHOICES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (SNAKE, 'Snake')
        )


	GENDER_CHOICES = (

		(MALE, "Male"),
		(FEMALE, "Female")

		)



	category = models.CharField(max_length=10,choices = ANIMAL_CHOICES, default= DOG)
	name = models.CharField(max_length=120, null = False, blank = False)
	age = models.CharField(max_length=120, null = False, blank = False)
	gender = models.CharField(choices= GENDER_CHOICES, max_length=120, null = False, blank = False)
	description = models.TextField(max_length=120, null = False, blank = False)
	photo = models.ImageField("photo", upload_to="media/")
	

	def get_absolute_url(self):
		#return f"/restaurants/{self.slug}"
		return reverse("animals:detail", kwargs= {"slug":self.slug})
	
        


	def __str__(self):
		return self.name
