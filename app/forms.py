from django import forms
from .models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User   
        fields =("username",'email',"password1","password2")
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.TextInput())
	

class blog_form(forms.ModelForm):
	class Meta:
		model = blog
		fields = '__all__'

	title=forms.CharField(widget=forms.TextInput({'placeholder':"Enter title"}))
	content=forms.CharField(widget=forms.TextInput({"placeholder":"write content here"}))
	image=forms.ImageField()
	date=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
	
		
		