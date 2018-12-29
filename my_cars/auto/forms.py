from django import forms
from .models import Advert

class PostForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ('maker', 'automodel', 'body', 'color', 'year', 'price', 'pic')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15)



