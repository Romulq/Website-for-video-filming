from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from .views import HomeView, WorksView, OrderView, CalcView, VideoView, TypeVideoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('works/', WorksView.as_view(), name='works'),
    path('order/', OrderView.as_view(), name='order'),
    path('order/calc', CalcView.as_view(), name='calc'),
    path('video/', VideoView.as_view(), name='video'),
    path('video/type', TypeVideoView.as_view(), name='typevideo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)