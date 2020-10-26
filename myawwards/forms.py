from .models import Projects,Rates,Profile
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Projects
        exclude=['user','design','usability','content']

class RateForm(forms.ModelForm):
    class Meta:
        model=Rates
        exclude=['user','project']


class UpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']