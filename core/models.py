from django.db import models
from django.utils.text import slugify

# Create your models here.

# Abstract base model for common fields
class TimeStamped(models.Model):
    """
    Abstract base model for models that need created and updated timestamps.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True



class SiteSettings(TimeStamped):
    """
    Helper for storing company information, contact details, and social media links.
    This model is designed to be a singleton, ensuring that only one instance exists to manage site-wide settings.
    """
    # Company information fields
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    company_name_initials = models.CharField(max_length=10, null=True, blank=True, verbose_name="Company Name Initials")

    # Logo fields with optional CSS for styling
    logo_light = models.ImageField(upload_to='site_settings/', null=True, blank=True, verbose_name="Light Logo")
    logo_dark = models.ImageField(upload_to='site_settings/', null=True, blank=True, verbose_name="Dark Logo")

    # Contact information
    contact_email = models.EmailField(null=True, blank=True, verbose_name="Contact Email")
    contact_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Contact Phone")
    contact_address = models.TextField(null=True, blank=True, verbose_name="Contact Address")
    contact_address_map_url = models.URLField(null=True, blank=True, verbose_name="Contact Address Map URL")

    # Social media links
    whatsapp_url = models.URLField(null=True, blank=True, verbose_name="WhatsApp URL")
    instagram_url = models.URLField(null=True, blank=True, verbose_name="Instagram URL")
    linkedin_url = models.URLField(null=True, blank=True, verbose_name="LinkedIn URL")
    youtube_url = models.URLField(null=True, blank=True, verbose_name="YouTube URL")
    facebook_url = models.URLField(null=True, blank=True, verbose_name="Facebook URL")
    x_url = models.URLField(null=True, blank=True, verbose_name="X URL")

    class Meta:
        verbose_name = "Global Site Settings"
    
    def __str__(self):
        return self.company_name

    # Singleton pattern to ensure only one instance of SiteSettings exists
    def save(self, *args, **kwargs):
        self.pk = 1  # Force primary key to always be 1
        super(SiteSettings, self).save(*args, **kwargs)
