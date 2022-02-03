from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import HomeView, WorksView, OrderView, CalcView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('works/', WorksView.as_view(), name='works'),
    path('order/', OrderView.as_view(), name='order'),
    path('order/calc', CalcView.as_view(), name='calc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)