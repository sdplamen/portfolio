from django.shortcuts import render
from resume.mixins import get_personal_info
from resume.models import PersonalInfo, WorkExperience, ProfessionalSkill, EducationTraining, LanguageSkill, PortfolioLink


# Create your views here.
def get_item(dictionary, key):
    return dictionary.get(key)

# def resume(request):
#     personal_info = PersonalInfo.objects.first()
#     work_experience = WorkExperience.objects.all()
#     education_training = EducationTraining.objects.all()
#     mother_tongue_obj = LanguageSkill.objects.filter(is_mother_tongue=True).first()
#     foreign_languages_objs = LanguageSkill.objects.filter(is_mother_tongue=False).order_by('language')
#     portfolio_links = PortfolioLink.objects.filter(personal_info=personal_info)
#     all_skills_queryset = Skill.objects.all().order_by('category', 'name')
#     all_skills_dict = {skill.name: skill for skill in all_skills_queryset}
#
#     development_skill_categories = [
#         'web_design_front_end', 'backend_skills', 'computer_science_programming',
#         'databases', 'data_structures', 'devops',
#     ]
#     graphic_design_skill_categories = [
#         'graphic_design',
#     ]
#
#     development_skills_by_category = {}
#     graphic_design_skills_by_category = {}
#
#     for skill in all_skills_queryset:
#         if skill.category in development_skill_categories:
#             if skill.category not in development_skills_by_category:
#                 development_skills_by_category[skill.category] = []
#             development_skills_by_category[skill.category].append(skill.name)
#         elif skill.category in graphic_design_skill_categories:
#             if skill.category not in graphic_design_skills_by_category:
#                 graphic_design_skills_by_category[skill.category] = []
#             graphic_design_skills_by_category[skill.category].append(skill.name)
#
#     context = {
#         'personal_info': personal_info,
#         'work_experience': work_experience,
#         'education_training': education_training,
#         'mother_tongue_obj': mother_tongue_obj,
#         'foreign_languages_objs': foreign_languages_objs,
#         'portfolio_links': portfolio_links,
#         'development_skills': development_skills_by_category,
#         'graphic_design_skills': graphic_design_skills_by_category,
#         'all_skills_dict': all_skills_dict,
#     }
#
#     return render(request, 'resume.html', context)

def resume(request):
    personal_info = get_personal_info(request)
    context = {
        'personal_info': personal_info,
    }
    return render(request, 'resume.html', context)


def contact_info_view(request):
    personal_info = get_personal_info(request)
    return render(request, 'contact_info.html', {'personal_info': personal_info})


def work_experience_view(request):
    personal_info = get_personal_info(request)
    work_experience = WorkExperience.objects.all()
    context = {
        'personal_info': personal_info,
        'work_experience': work_experience,
    }
    return render(request, 'work_experience.html', context)


def professional_skills_view(request):
    personal_info = get_personal_info(request)
    all_skills_queryset = ProfessionalSkill.objects.all().order_by('category', 'name')

    development_skills = {}
    graphic_design_skills = {}

    development_categories = {'Web Design', 'Frontend', 'Backend', 'Computer Science Programming', 'Databases',
                              'Data Structures', 'DevOps'}
    graphic_design_categories = {'2D Graphic Design', '3D Graphic Design', 'Interior Design', 'Brand Identity',
                                 'UX / UI Design', 'Instructional Design', 'Video Editing', 'Scanning'}

    for skill in all_skills_queryset:
        skill.progress_percent = skill.progress * 10
        if skill.category in development_categories:
            development_skills.setdefault(skill.category, []).append(skill)
        elif skill.category in graphic_design_categories:
            graphic_design_skills.setdefault(skill.category, []).append(skill)

    context = {
        'personal_info': personal_info,
        'development_skills': development_skills,
        'graphic_design_skills': graphic_design_skills,
    }
    return render(request, 'professional_skills.html', context)


def education_training_view(request):
    personal_info = get_personal_info(request)
    education_training = EducationTraining.objects.all()
    context = {
        'personal_info': personal_info,
        'education_training': education_training,
    }
    return render(request, 'education_training.html', context)


def portfolio_view(request):
    personal_info = get_personal_info(request)
    portfolio_links = PortfolioLink.objects.filter(personal_info=personal_info) if personal_info else None
    context = {
        'personal_info': personal_info,
        'portfolio_links': portfolio_links,
    }
    return render(request, 'portfolio.html', context)


def language_skills_view(request):
    personal_info = get_personal_info(request)
    mother_tongue_obj = LanguageSkill.objects.filter(is_mother_tongue=True).first()
    foreign_languages_objs = LanguageSkill.objects.filter(is_mother_tongue=False).order_by('language')
    context = {
        'personal_info': personal_info,
        'mother_tongue_obj': mother_tongue_obj,
        'foreign_languages_objs': foreign_languages_objs,
    }
    return render(request, 'language_skills.html', context)