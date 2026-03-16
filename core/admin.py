from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SiteSettings

# Register your models here.
@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ('company_name', 'contact_email', 'contact_phone', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('company_name', 'company_name_initials')
        }),
        ('Logos', {
            'fields': ('logo_light', 'logo_dark')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'contact_address', 'contact_address_map_url')
        }),
        ('Social Media Links', {
            'fields': (
                'whatsapp_url',
                'instagram_url',
                'linkedin_url',
                'youtube_url',
                'facebook_url',
                'x_url'
            )
        }),
    )
