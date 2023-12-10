from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image, Video

# Create your views here.

def home(request):
    images = Image.objects.order_by('-id')[:4]
    videos = Video.objects.order_by('-id')[:4]
    
    return render(request, 'index.html', {'images':images, 'videos': videos})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'pages/image_list.html', {'images': images})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'pages/video_list.html', {'videos': videos})

def upload_image(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        Image.objects.create(title=title, image=image, description=description)
        messages.success(request, 'Video has been uploaded successfully')
        
        return redirect('image_list')
    return render(request, 'upload/upload_image.html')

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video = request.FILES.get('video')
        video_link = request.POST.get('video_link')
        description = request.POST.get('description')

        if not video and not video_link:
            # Handle the case where neither video nor video_link is provided
            messages.error(request, 'Please provide either a video file or a video link.')
            return render(request, 'upload/upload_video.html')

        # Create the Video instance based on the provided input
        if video:
            Video.objects.create(title=title, video=video, description=description)
            messages.success(request, 'Video has been uploaded successfully')
        else:
            Video.objects.create(title=title, video_link=video_link, description=description)
            messages.success(request, 'Video has been uploaded successfully')

        return redirect('video_list')

    return render(request, 'upload/upload_video.html')

