from django.shortcuts import render
from resume.models import UserProfile, WorkExperience, Education, SkillCategory, Language, PortfolioLink


# Create your views here.
def resume(request):
    user_profile = UserProfile.objects.first()
    work_experiences = WorkExperience.objects.all().order_by('-start_date')
    education_entries = Education.objects.all().order_by('-start_date')
    skill_categories = SkillCategory.objects.all().prefetch_related('skills')
    languages = Language.objects.all().order_by('language_name')
    portfolio_links = PortfolioLink.objects.all()

    context = {
        'user_profile': user_profile,
        'work_experiences': work_experiences,
        'education_entries': education_entries,
        'skill_categories': skill_categories,
        'languages': languages,
        'portfolio_links': portfolio_links,
    }
    return render(request, 'resume_detail.html', context)
