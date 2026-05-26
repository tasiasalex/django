from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"), 
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("posts/tag/<slug:tag_slug>", views.posts_by_tag, name="posts-by-tag"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    
]