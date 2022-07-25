from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['sport', 'location', 'date', 'time', 'content']

    widgets = {
        'sport': forms.TextInput(attrs={'class': 'sport-field', 'placeholder': 'ur ugly'}),
        'location': forms.TextInput(attrs={'class': 'location-field'}),
        'date': forms.DateInput(attrs={'class': 'date-field'}),
        'time': forms.TimeInput(attrs={'class': 'time-field'}),
        'content': forms.Textarea(attrs={'class': 'content-field'})
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


