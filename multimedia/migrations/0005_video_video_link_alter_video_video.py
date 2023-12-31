# Generated by Django 4.1.13 on 2023-12-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("multimedia", "0004_alter_video_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="video_link",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(
                blank=True, default="assets\\video.mp4", null=True, upload_to="videos"
            ),
        ),
    ]
