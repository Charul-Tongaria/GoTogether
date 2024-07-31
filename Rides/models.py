from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class Ride(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    leaving_from = models.CharField(max_length=100)
    going_to = models.CharField(max_length=100)
    date_of_departure = models.DateField()
    num_passengers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.leaving_from} to {self.going_to} on {self.date_of_departure}"

class CustomUser(AbstractUser):
    # Adding related_name to avoid clashes with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    pass 