from django.shortcuts import render, redirect
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

def upload_page(request):
    return render(request, 'upload/upload_page.html')

def upload_image(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        Image.objects.create(title=title, image=image, description=description)
        return redirect('image_list')
    return render(request, 'upload/upload_image.html')

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video = request.FILES.get('video')
        description = request.POST.get('description')
        Video.objects.create(title=title, video=video, description=description)
        return redirect('video_list')
    return render(request, 'upload/upload_video.html')
