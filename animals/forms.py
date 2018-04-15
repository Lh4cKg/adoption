from django import forms
from .models import Animals, Comment


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
		"location",
		"sex",
		"description",
		"photo",
		
		
		
		
		
		]


class CommentForm(forms.ModelForm):
	# text = TextField(max_length = 240, blank = False, null = False, default = "o")

	class Meta:
		model = Comment
		fields = ( 'text',)