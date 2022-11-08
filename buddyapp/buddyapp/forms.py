from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from utmostmining.members.models import Members

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'required': '',
            'name': 'first_name',
            'id': 'first_name',
            'type': 'text',
            'class': 'form-control form-control-user', 
            'placeholder': 'First Name',
            'maxlength': '',
            'minlength': '3', 

            })
        self.fields['last_name'].widget.attrs.update({
            'required': '',
            'name': 'last_name',
            'id': 'last_name',
            'type': 'text',
            'class': 'form-control form-control-user', 
            'placeholder': 'Last Name',
            'maxlength': '',
            'minlength': '3', 

            })
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-control form-control-user', 
            'placeholder': 'Username',
            'maxlength': '',
            'minlength': '3', 

            })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-control form-control-user', 
            'placeholder': 'Email Address',
            'maxlength': '',
            'minlength': '6', 

            })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control form-control-user', 
            'placeholder': 'Password',
            'maxlength': '',
            'minlength': '3', 

            })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-control form-control-user', 
            'placeholder': 'Repeat Password',
            'maxlength': '',
            'minlength': '3', 

            })
        
            
         
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


