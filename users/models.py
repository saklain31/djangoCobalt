from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()


class Event(models.Model):
	name = models.TextField()

	class Meta:
		permissions = (
			('add_ev', 'Add event'),
			('del_ev','Delete event'),
			('edit_ev','Edit event'),
		)

	def __str__(self):
		return self.name