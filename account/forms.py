from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	password_two = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User 
		fields = ['username','email']

	def clean_password_two(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password_two']:
			raise forms.ValidationErrors('Entered Password Donot Match')
			#this is definately somethinf you do in the backend. use Javascript
		return cd['password_two']