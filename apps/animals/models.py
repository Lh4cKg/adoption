from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.shortcuts import get_object_or_404
from ..accounts.models import UserModel


class Animals(models.Model):
    DOG = "dog"
    CAT = "cat"
    MALE = "m"
    FEMALE = "f"

    ANIMAL_CHOICES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        
    )

    GENDER_CHOICES = (

        (MALE, "Male"),
        (FEMALE, "Female")

    )

    category = models.CharField(max_length=10, choices=ANIMAL_CHOICES, default=DOG)
    name = models.CharField(max_length=120, null=False, blank=False)
    location = models.CharField(max_length=120, null=False, blank=False)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=120, null=False, blank=False)
    description = models.TextField(max_length=120, null=False, blank=False)
    photo = models.ImageField("photo", upload_to="media/", null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def animal_pre_save_receiver(sender, instance, *args, **kwargs):
    print("saving")
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def animal_post_save_receiver(sender, instance, created, *args, **kwargs):
# 		print("saved")
# 		print(instance.timestamp)


pre_save.connect(animal_pre_save_receiver, sender=Animals)


# post_save.connect(animal_post_save_receiver,  sender= Animals)


class Comment(models.Model):
    text = models.TextField(max_length=300, blank=False, null=False)
    post = models.ForeignKey('animals.Animals', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey("accounts.UserModel", on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
