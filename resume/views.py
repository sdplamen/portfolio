from django.shortcuts import render
from resume.models import PersonalInfo, WorkExperience, Skill, EducationTraining, LanguageSkill, PortfolioLink


# Create your views here.
def get_item(dictionary, key):
    return dictionary.get(key)

def resume(request):
    personal_info = PersonalInfo.objects.first()
    work_experience = WorkExperience.objects.all()
    education_training = EducationTraining.objects.all()
    mother_tongue_obj = LanguageSkill.objects.filter(is_mother_tongue=True).first()
    foreign_languages_objs = LanguageSkill.objects.filter(is_mother_tongue=False).order_by('language')
    portfolio_links = PortfolioLink.objects.filter(personal_info=personal_info)
    all_skills_queryset = Skill.objects.all().order_by('category', 'name')
    all_skills_dict = {skill.name: skill for skill in all_skills_queryset}

    development_skill_categories = [
        'web_design_front_end', 'backend_skills', 'computer_science_programming',
        'databases', 'data_structures', 'devops',
    ]
    graphic_design_skill_categories = [
        'graphic_design',
    ]

    development_skills_by_category = {}
    graphic_design_skills_by_category = {}

    for skill in all_skills_queryset:
        if skill.category in development_skill_categories:
            if skill.category not in development_skills_by_category:
                development_skills_by_category[skill.category] = []
            development_skills_by_category[skill.category].append(skill.name)
        elif skill.category in graphic_design_skill_categories:
            if skill.category not in graphic_design_skills_by_category:
                graphic_design_skills_by_category[skill.category] = []
            graphic_design_skills_by_category[skill.category].append(skill.name)

    context = {
        'personal_info': personal_info,
        'work_experience': work_experience,
        'education_training': education_training,
        'mother_tongue_obj': mother_tongue_obj,
        'foreign_languages_objs': foreign_languages_objs,
        'portfolio_links': portfolio_links,
        'development_skills': development_skills_by_category,
        'graphic_design_skills': graphic_design_skills_by_category,
        'all_skills_dict': all_skills_dict,
    }

    return render(request, 'resume.html', context)
