from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'after', 'short_description', 'text', 'pab_data']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'название фильма'}),
            'after': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор рецензии'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Актеры'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'pab_data': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'дата публикации'}),
        }