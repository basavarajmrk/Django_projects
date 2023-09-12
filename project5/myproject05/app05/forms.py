# forms.py in your app
from django import forms
from .models import UserInput  # If you have a model

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput  # Use your model if you have one
        fields = ['input_field']
        fields = ['input_field']  # Specify the fields you want to collect
