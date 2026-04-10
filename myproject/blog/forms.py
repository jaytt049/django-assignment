from django import forms
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category', 'tags', 'image', 'file']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
class CSVUploadForm(forms.Form):
    file = forms.FileField()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']