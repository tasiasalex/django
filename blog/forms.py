from django import forms
from .models import Comment

# Creo el formulari per als comentaris basat en el model que ja tinc
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        # Trec el camp 'post' perquè no vull que l'usuari l'hagi de triar manualment
        # El post s'assignarà automàticament des de la vista
        exclude = ["post"]
        
        # Cambio els noms dels camps perquè a la web es vegin més macos i en català
        labels = {
            "user_name": "El teu nom",
            "user_email": "El teu correu",
            "text": "El teu comentari"
        }
