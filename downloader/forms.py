from django import forms
from pytube import exceptions as p
from .validator import validate_url

class HomeForm(forms.Form):
    def badURL(self):
        if p.RegexMatchError(self.URL) == 'True':
            raise forms.ValidationError('Bad URL')
        return 'Good URL'
    
    URL = forms.URLField(validators=[validate_url],widget=forms.TextInput(attrs={'class': 'url', 'placeholder':'YouTube URL'}))
    