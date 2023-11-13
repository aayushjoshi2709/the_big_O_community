from django.forms import Form,PasswordInput,EmailField,CharField


class LoginForm(Form):
    username = CharField(label='email',max_length=100)
    password = CharField(label='password',widget=PasswordInput)

class RegistrationFrom(Form):
    first_name = CharField(label='First Name', max_length=50)
    last_name = CharField(label='Last Name', max_length=50)
    username = CharField(label='username',max_length=100)
    email = EmailField(label='email')
    password = CharField(label='password',widget=PasswordInput)

