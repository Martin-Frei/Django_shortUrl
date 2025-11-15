from django import forms
from short.models import shortUrl

class shortUrlForm(forms.ModelForm):
    
    class Meta:
        model = shortUrl
        fields = ['longUrl']
        
        
