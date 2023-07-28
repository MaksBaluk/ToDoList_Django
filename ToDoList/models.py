from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users.models import CustomUser


# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ToDoList')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'ToDoList'
        verbose_name_plural = 'ToDoLists'
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.title} {self.user.username}'

    def save(self, *args, **kwargs):
        if not self.slug:  # Перевірка, чи вже є значення в полі slug
            unique_id = str(uuid4())
            self.slug = slugify(f'{self.user.username}-task-{unique_id}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'task_slug': self.slug, 'user_slug': self.user.slug})
