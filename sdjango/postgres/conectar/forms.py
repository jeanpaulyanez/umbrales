from django import forms
from conectar.models import mcafee_updatedstate
class entrausuario(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12','id':'first-name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12','id':'first-name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12','id':'first-name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12','id':'first-name'}))
    user  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12','id':'first-name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-7 col-xs-12','id':'first-name'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-7 col-xs-12','id':'first-name'}))
    
class umbrales(forms.Form):
    uno = forms.CharField(widget=forms.TextInput(attrs={'class': 'knob','data-width':'110','data-height':'120','data-displayPrevious':'true','data-fgColor':'#26B99A','data-skin':'tron','data-thickness':'.2','value':'75'}))
