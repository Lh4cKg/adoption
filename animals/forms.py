from django import forms
from .models import Animals


# class AnimalCreate(forms.Form):

# 	name            = forms.CharField()
# 	breed           = forms.CharField()
# 	age             = forms.CharField()
# 	gender          = forms.CharField()





class AnimalCreateForm(forms.ModelForm):
	# category = forms.CharField(required= False, validators=[validate_category])
	# email = forms.EmailFi.eld()
	class Meta:
		model = Animals
		fields =[
		"category", 
		"name", 
		"age",
		"gender",
		"description",
		"photo",
		
		]



# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()