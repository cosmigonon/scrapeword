from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=False, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(verbose_name="email address", blank=False, unique=True)
    backup_email = models.EmailField(
        verbose_name="secondary email", blank=True, null=True, unique=True
    )
    profile_pic = models.ImageField(verbose_name="avatar", blank=True, null=True)
    bio = models.CharField(
        verbose_name="user_bio", max_length=160, blank=True, null=True
    )
    location = models.CharField(max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "is_staff", "is_superuser"]

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username
