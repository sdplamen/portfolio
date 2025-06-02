from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    contact_address = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()
    target_employment = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PortfolioLink(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='portfolio_links')
    domain = models.CharField(max_length=100)
    url = models.URLField()

class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)

class Skill(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class EducationTraining(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)

class LanguageSkill(models.Model):
    language = models.CharField(max_length=50)
    listening = models.CharField(max_length=5)
    reading = models.CharField(max_length=5)
    conversation = models.CharField(max_length=5)
    oral_exposure = models.CharField(max_length=5)
    writing = models.CharField(max_length=5)
    is_mother_tongue = models.BooleanField(default=False)
