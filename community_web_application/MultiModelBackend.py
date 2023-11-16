from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import Author
class MultiModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.filter(username=username).first()
        if user is not None and user.check_password(password):
            return user
        author = Author.objects.filter(username=username).first()
        if author is not None and author.check_password(password):
            return author
        return None