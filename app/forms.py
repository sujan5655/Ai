from django import forms
from .models import Projects,Gallery
from .models import Feedback

class Projectform(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'description','image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input bg-gray-100 border-2 border-gray-300 rounded-lg p-2 w-3/4 text-blue-600',
                'placeholder': 'Enter title here...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea bg-gray-100 border-2 border-gray-300 rounded-lg p-2 w-3/4 text-blue-600',
                'placeholder': 'Enter description here...',
                'rows': 4
            }),
           
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-input bg-gray-100 border-2 border-gray-300 rounded-lg p-2 w-3/4',
            }),
        }

class Galleryform(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image','title')
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-input bg-gray-100 border-2 border-gray-300 rounded-lg p-2 w-3/4',
            }),
             'title': forms.TextInput(attrs={
                'class': 'form-input bg-gray-100 border-2 border-gray-300 rounded-lg p-2 w-3/4 text-blue-600',
                'placeholder': 'Enter title here...'
            }),
        }
        
from django import forms
from .models import Feedback

from django import forms
from .models import Feedback
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'comments', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your full name', 
                'style': 'border: 1px solid black; padding: 10px; border-radius: 5px; color: black;',
            }),
            'comments': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Share your thoughts or feedback here', 
                'rows': 5, 
                'style': 'border: 1px solid black; padding: 10px; border-radius: 5px; color: black;',
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control', 
                'style': 'border: 1px solid black; padding: 10px; border-radius: 5px; color: black;',
            }),
        }
        labels = {
            'name': 'Your Name',
            'comments': 'Your Comments',
            'rating': 'Rating (1 to 5)',
        }
        help_texts = {
            'rating': 'Choose a rating from 1 (poor) to 5 (excellent).',
        }
