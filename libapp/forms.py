from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.Form):

    name=forms.CharField(max_length=50)
    Roll_number=forms.IntegerField()
    Percentage=forms.FloatField()


class UserForm(UserCreationForm):
    class Meta:
        model=User

        fields=['username','first_name','last_name','email']    