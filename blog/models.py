from django.db import models
from django.core.validators import MinLengthValidator

# Model per a les etiquetes dels posts (ex: Viatges, Tecnologia)
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    # Això serveix per veure el nom del tag al panell d'admin en lloc de "Tag object"
    def __str__(self):
        return self.caption

# Model per als autors de les entrades
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    # Mostrem el nom complet de l'autor a l'admin
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model principal per a les entrades del blog
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200) # Resum curt de la entrada
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    # L'slug és l'URL maca (ex: el-meu-viatge), unique=True per no repetir-les
    slug = models.SlugField(unique=True, db_index=True)
    # Posem un validador perquè el contingut no sigui massa curt
    content = models.TextField(validators=[MinLengthValidator(10)])
    
    # Relació d'un autor per cada post. Si s'esborra l'autor, el post es queda sense autor (null)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    
    # Un post pot tenir molts tags i un tag pot estar en molts posts
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

# Model per guardar els comentaris que deixen els lectors
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    
    # Connectem el comentari amb un Post específic. 
    # Si s'esborra el post, s'esborren tots els seus comentaris (CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name}: {self.text[:20]}..."
