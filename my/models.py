from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
