from django.contrib import admin

from resume.models import WorkExperience, ProfessionalSkill, PersonalInfo, PortfolioLink, EducationTraining, LanguageSkill


# Register your models here.
@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'summary', 'contact_address', 'contact_phone', 'email', 'target_employment', 'profile_picture'
)

@admin.register(PortfolioLink)
class PortfolioLinkAdmin(admin.ModelAdmin):
    list_display = ('personal_info', 'domain', 'url')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')

@admin.register(ProfessionalSkill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'progress')

@admin.register(EducationTraining)
class EducationTrainingAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')

@admin.register(LanguageSkill)
class LanguageSkillAdmin(admin.ModelAdmin):
    list_display = ('language', 'listening', 'reading', 'conversation', 'oral_exposure', 'writing', 'is_mother_tongue')