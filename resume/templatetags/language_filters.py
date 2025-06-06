from django import template

register = template.Library()
@register.filter
def proficiency_level(value):
    if value == 0:
        return 'Beginner' #'Beginner (No exposure)'
    elif value <= 2:
        return 'A1' #'A1 (Beginner)'
    elif value <= 4:
        return 'A2 '#A2 (Elementary)'
    elif value <= 6:
        return 'B1' #'B1 (Intermediate)'
    elif value <= 8:
        return 'B2' #'B2 (Upper Intermediate)'
    elif value <= 9:
        return 'C1' #'C1 (Advanced)'
    elif value == 10:
        return 'C2' #'C2 (Proficient)'
    else:
        return 'N/A'