from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"] # No volem que l'usuari trii el post, ja sabem on és
        labels = {
            "user_name": "El teu nom",
            "user_email": "El teu correu",
            "text": "El teu comentari"
        }