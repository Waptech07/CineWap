# Generated by Django 4.1.13 on 2023-12-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("multimedia", "0003_alter_image_image_alter_video_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(default="assets\\video.mp4", upload_to="videos"),
        ),
    ]
