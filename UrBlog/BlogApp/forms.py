from django import forms
from django.contrib.auth.models import User
from .models import Comment
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from BlogApp.validators import email_validation

# ----- Signup ------

class Signup(UserCreationForm):
    email=forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'class':'w-100','placeholder':'Enter your email...'}),validators=[email_validation])
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-100','placeholder':'Enter password...'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-100','placeholder':'Confirm password...'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'w-100','placeholder':'Enter username...'})}

# ---- login ----

class Login(AuthenticationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'w-100','placeholder':'Enter Username...'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-100','placeholder':'Enter password...'}),error_messages={'required':'Please enter password'})

    class Meta:
        model=User
        fields=['username','password']


class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['message']
        # requireds={'message':False} 
        widgets={'message':forms.Textarea(attrs={'class':'comment-area','placeholder':'Enter your valuable comment...'})}


