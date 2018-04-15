from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel
from django.views.generic.edit import UpdateView



class SignUpForm(UserCreationForm):
   
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = UserModel
        fields = ( 'nickname', 'first_name', 'last_name', "location",'email', 'password1', 'password2')


class UpdateProfile(forms.ModelForm):
	
	
	
	class Meta:
		model = UserModel
		fields = ( 'nickname', 'first_name', 'last_name', "location")
