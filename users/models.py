from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class CustomUser(AbstractUser):
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.username}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'user_slug': self.slug})
