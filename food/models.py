
from django.db import models
from django.urls import reverse
import uuid


class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='photos/foods')
    address = models.CharField(max_length=100, blank=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
