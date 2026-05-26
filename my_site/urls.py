from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # Ruta per entrar al panell d'administració de Django
    path('admin/', admin.site.urls),
    
    # Connecto les URLs del projecte amb les de la meva app 'blog'
    # Així, qualsevol ruta buida o que no sigui admin anirà al blog
    path('', include('blog.urls')),
]

# Configuració especial per a que els fitxers estàtics funcionin 
# quan el mode DEBUG està apagat (per exemple, a producció)
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
