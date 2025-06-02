from django.shortcuts import render
from resume.models import PersonalInfo, WorkExperience, Skill, EducationTraining, LanguageSkill, PortfolioLink


# Create your views here.
def resume(request):
    personal_info = PersonalInfo.objects.first()
    work_experience = WorkExperience.objects.all()
    professional_skills = Skill.objects.all()
    education_training = EducationTraining.objects.all()
    mother_tongue_obj = LanguageSkill.objects.filter(is_mother_tongue=True).first()
    foreign_languages_objs = LanguageSkill.objects.filter(is_mother_tongue=False).order_by('language')
    portfolio_links = PortfolioLink.objects.filter(personal_info=personal_info)

    context = {
        'personal_info': personal_info,
        'work_experience': work_experience,
        'professional_skills': professional_skills,
        'education_training': education_training,
        'mother_tongue_obj': mother_tongue_obj,
        'foreign_languages_objs': foreign_languages_objs,
        'portfolio_links': portfolio_links,  # And include this
    }

    return render(request, 'resume.html', context)
