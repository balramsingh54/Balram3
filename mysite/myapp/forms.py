from django import forms
from .models import *
class RegisterForm(forms.ModelForm):
	fname=forms.CharField()
	lname=forms.CharField()
	fathername=forms.CharField()
	addr=forms.CharField(widget=forms.Textarea)
	userid=forms.CharField()
	passwd=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Register
		fields='__all__'
class LoginForm(forms.ModelForm):
	userid=forms.CharField()
	passwd=forms.CharField(max_length=20,widget=forms.PasswordInput)
	class Meta:
		model=Register
		fields='__all__'
	