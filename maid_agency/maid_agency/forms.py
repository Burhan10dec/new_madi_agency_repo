from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from Agency.models import AgencyProfile
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email', 'password1', 'password2']



# class AgencyProfileForm(ModelForm):
# 	class Meta:
# 		model = AgencyProfile
# 		fields = '__all__'