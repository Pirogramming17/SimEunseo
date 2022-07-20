from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ideas"

urlpatterns = [
    path('', views.main, name='main'),
    path('register', views.register, name='register')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)