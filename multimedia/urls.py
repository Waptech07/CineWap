from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('images/', views.image_list, name='image_list'),
    path('videos/', views.video_list, name='video_list'),
    path('upload_page/', views.upload_page, name='upload_page'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_video/', views.upload_video, name='upload_video'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)