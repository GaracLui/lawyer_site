from .models import SiteSettings

def global_settings(request):
    """
    Context processor para agregar configuraciones globales a todas las plantillas.
    """
    settings = SiteSettings.objects.first()
    return {
        'settings': settings  # Asumiendo que solo hay una instancia de configuración
    }