from resume.models import PersonalInfo

def get_personal_info(request):
    lang_preference = request.GET.get('lang', 'first')
    if lang_preference == 'last':
        personal_info_qs = PersonalInfo.objects.all().order_by('-id')
    else:
        personal_info_qs = PersonalInfo.objects.all().order_by('id')

    personal_info = personal_info_qs.first()

    if personal_info:
        personal_info.visitor_count += 1
        personal_info.save()

    return personal_info