from django.urls import path
from resume import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.resume, name='resume'),
    path('contact/', views.contact_info_view, name='contact_info'),
    path('work-experience/', views.work_experience_view, name='work_experience'),
    path('skills/', views.professional_skills_view, name='professional_skills'),
    path('education/', views.education_training_view, name='education_training'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('languages/', views.language_skills_view, name='language_skills'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)