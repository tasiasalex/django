from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Configuro com es veuran els Posts al panell d'administració
class PostAdmin(admin.ModelAdmin):
    # Afegeixo filtres al lateral per buscar més fàcil per autor, tags o data
    list_filter = ("author", "tags", "date",)
    
    # Columnes que vull que es vegin a la llista principal d'entrades
    list_display = ("title", "date", "author",)
    
    # Això em serveix per a que el 'slug' s'escrigui sol mentre poso el títol
    prepopulated_fields = {"slug": ("title",)}

# Registro els models perquè surtin al panell de control de Django
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
