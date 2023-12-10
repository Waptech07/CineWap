import os
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default=os.path.join("assets", "image.png"), upload_to="images")
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

def validate_video_fields(value_dict):
    video_file = value_dict.get('video')
    video_link = value_dict.get('video_link')

    if not video_file and not video_link:
        raise ValidationError("Please provide either a video file or a video link, or both.")

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos", blank=True, null=True)
    video_link = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()

    def clean(self):
        validate_video_fields({'video': self.video, 'video_link': self.video_link})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
