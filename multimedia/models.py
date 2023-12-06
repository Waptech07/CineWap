import os
from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default=os.path.join("assets", "image.png"), upload_to="images")
    description = models.TextField()

    def __str__(self):
            return f"{self.title}"

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(default=os.path.join("assets", "video.mp4"), upload_to="videos")
    description = models.TextField()

    def __str__(self):
            return f"{self.title}"    
