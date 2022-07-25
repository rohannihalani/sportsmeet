
from django.db import models as real_models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(real_models.Model):
    sport = real_models.CharField(max_length=100)
    location = real_models.CharField(max_length=200)
    date = real_models.DateField(default=timezone.now)
    time = real_models.TimeField(default=timezone.now)
    content = real_models.TextField()
    author = real_models.ForeignKey(User, on_delete=real_models.CASCADE, null=True)
    date_posted = real_models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.sport
    
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    
    
