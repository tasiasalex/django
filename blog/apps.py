from django.apps import AppConfig

# Configuració bàsica de l'aplicació de blog
class BlogConfig(AppConfig):
    # Defineixo el tipus d'ID autoincremental que faran servir els models per defecte
    default_auto_field = 'django.db.models.BigAutoField'
    
    # El nom de l'app tal com està a la carpeta
    name = 'blog'
