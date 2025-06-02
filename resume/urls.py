from django.urls import path
from resume import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.resume, name='resume'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)