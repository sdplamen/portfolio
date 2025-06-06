from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.constraints import CheckConstraint


# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    contact_address = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()
    target_employment = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.name

class PortfolioLink(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='portfolio_links')
    domain = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.domain

class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class ProfessionalSkill(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    progress = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Progress percentage (0-10)"
    )

    def __str__(self):
        return self.name

class EducationTraining(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class LanguageSkill(models.Model):
    language = models.CharField(max_length=50)
    listening = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    reading = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    conversation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    oral_exposure = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    writing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    is_mother_tongue = models.BooleanField(default=False)

    def __str__(self):
        return self.language