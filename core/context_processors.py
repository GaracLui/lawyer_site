from .models import SiteSettings

def global_settings(request):
    """
    Context processor para agregar configuraciones globales a todas las plantillas.
    """
    return {
        'settings': SiteSettings.objects.first()  # Asumiendo que solo hay una instancia de configuración
    }