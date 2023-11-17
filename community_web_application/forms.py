from django.forms import Form,PasswordInput,CharField,ValidationError, ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Author,Blog,Image
from django import forms
class LoginForm(Form):
    username = CharField(label='username',max_length=100)
    password = CharField(label='password',widget=PasswordInput)
class RegistrationFrom(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Author.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Author.objects.filter(username=username).exists():
            raise ValidationError('This username address is already in use.')
        return username
    class Meta:
        model=Author
        fields = ['first_name', 'last_name' ,'username','email','password1','password2']

class RegistrationUpdationForm(ModelForm):
    class Meta:
        model=Author
        fields = ['first_name', 'last_name' ,'username','email']

class UpdatePasswordForm(PasswordChangeForm):
    class Meta:
        model=Author

class AddBlogForm(forms.ModelForm):

    class Meta:
        model=Blog
        fields= ['title','description','estimated_time_to_read','content','tags']
        