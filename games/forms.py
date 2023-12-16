from django import forms
from .models import Review, Games

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

class AgregarJuegoForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = (
            'title',
            'author',
            'price',
            'cover',
        )