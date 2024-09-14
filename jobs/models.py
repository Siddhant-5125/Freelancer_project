from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class FreeLancer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    skills = models.TextField(blank=True)
    tagline = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return f"{self.id} | {self.name}"


class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=100, blank=True)
    skills_required = models.TextField(blank=True)
    project_description = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True)
    applications = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.id} | {self.name}"