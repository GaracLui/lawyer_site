from django.shortcuts import render
from django.conf import settings
from .models import SiteSettings

# Create your views here.
def base(request):
    site_settings = SiteSettings.objects.first()  # Get the singleton instance of SiteSettings
    context = {
        'site_settings': site_settings,
    }
    return render(request, 'core/base.html', context)
