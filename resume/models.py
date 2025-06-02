from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    summary = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    target_employment = models.TextField()
    profile_image = models.ImageField(upload_to='static/img/', blank=True, null=True)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title} at {self.company}'

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.degree} from {self.school}'

class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'category')

class Language(models.Model):
    language_name = models.CharField(max_length=50, unique=True)
    level_listening = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    level_reading = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    level_conversation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    level_oral_exposure = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    level_writing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def get_cefr_level(self, level_value):
        if level_value >= 9:
            return 'C2'
        elif level_value >= 8:
            return 'C1'
        elif level_value >= 7:
            return 'B2'
        elif level_value >= 6:
            return 'B1'
        elif level_value >= 5:
            return 'A2'
        elif level_value >= 4:
            return 'A1'
        else:
            return 'Beginner'

    def __str__(self):
        return self.language_name

class PortfolioLink(models.Model):
    icon = models.ImageField(upload_to='portfolio_icons/')
    domain = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.domain
