from django.urls import path
from . import views

urlpatterns = [
    # La pàgina principal que ensenya els últims posts
    path("", views.starting_page, name="starting-page"),
    
    # Llista de tots els posts del blog
    path("posts", views.posts, name="posts-page"), 
    
    # Detall d'un post concret fent servir el 'slug' (l'URL maca)
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    
    # Per filtrar posts per una etiqueta o categoria (tag)
    path("posts/tag/<slug:tag_slug>", views.posts_by_tag, name="posts-by-tag"),
    
    # La vista per als posts guardats per llegir més tard (feta amb una classe)
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    
    path("authors", views.AuthorListView.as_view(), name="authors-page"),
    
    path("authors/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail-page"),
]
