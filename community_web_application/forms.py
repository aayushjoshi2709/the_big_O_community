from django.forms import Form,PasswordInput,EmailField,CharField


class LoginForm(Form):
    email = EmailField(label='email')
    password = CharField(label='password',widget=PasswordInput)

class RegistrationFrom(Form):
    first_name = CharField(label='First Name', max_length=50)
    last_name = CharField(label='Last Name', max_length=50)
    phone_number = CharField(label='Phone No',max_length=10)
    email = EmailField(label='email')
    password = CharField(label='password',widget=PasswordInput)

