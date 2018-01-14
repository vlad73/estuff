
# Create your models here.

# var newStoneAdvertSchema = new mongoose.Schema({
#     userid: String,
#     advertid: String,
#     registration: Number,
#     dateupdated: Number,
#     dateextended: Number,
#     permissions: String,
#     group: String,
#     active: Boolean,
#     seenbyotherusers: Number,
#     item: String,
#     stone_weight: String,
#     shape: String,
#     color: String,
#     clarity: String,
#     certificate: String,
#     description: String,
#     name: String,
#     phone: String,
#     mail: String,
#     skype: String,
#     country: String,
#     city: String,
#     images: [],
#     price: Number
# });
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30, blank=True)
    skype = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'username'

    def __str__(self):  # __unicode__ for Python 2
        return self.email
