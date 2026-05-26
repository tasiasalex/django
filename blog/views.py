from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Post, Tag
from .forms import CommentForm

# Pàgina d'inici: només vull ensenyar els 3 posts més nous
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

# Llista completa de posts, ordenats per data (els nous primer)
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    all_tags = Tag.objects.all()
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
        "all_tags": all_tags
    })

# Vista detallada d'un post. Gestiona també el formulari de comentaris.
def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    
    # Comprovo si aquest post ja està a la llista de "llegir més tard" de la sessió
    stored_posts = request.session.get("stored_posts")
    if stored_posts is not None:
        is_saved_for_later = identified_post.id in stored_posts
    else:
        is_saved_for_later = False

    # Si l'usuari envia un comentari (mètode POST)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = identified_post # Assigno el comentari a aquest post concret
            comment.save()
            # Refresco la pàgina per veure el comentari nou
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
    else:
        # Si només entra a veure el post, li dono el formulari buit
        comment_form = CommentForm()

    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all(),
        "comment_form": comment_form,
        "comments": identified_post.comments.all().order_by("-id"),
        "is_saved": is_saved_for_later 
    })

# Filtre de posts per etiqueta (tag)
def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, caption__iexact=tag_slug)
    filtered_posts = Post.objects.filter(tags=tag).order_by("-date")
    all_tags = Tag.objects.all() # Perquè el menú de tags no desaparegui
    
    return render(request, "blog/all-posts.html", {
        "all_posts": filtered_posts,
        "tag_name": tag.caption,
        "all_tags": all_tags
    })

# Faig servir una classe per gestionar la llista de "Llegir més tard" amb sessions
class ReadLaterView(View):
    # Mostra la llista de posts guardats
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = Post.objects.filter(id__in=stored_posts)
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)

    # Afegeix o treu un post de la llista (botó de guardar/eliminar)
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])
        
        # Si ja hi és el trec, si no hi és l'afegeixo
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        # Torno a la pàgina del post on estava l'usuari
        post = get_object_or_404(Post, id=post_id)
        return HttpResponseRedirect(reverse("post-detail-page", args=[post.slug]))
