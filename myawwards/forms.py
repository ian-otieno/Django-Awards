from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import UserProfile,Project, Rating

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_photo', 'phone_number']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_image', 'project_description', 'project_link']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']