from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# author information table
class Author(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50,unique=True, db_index=True)
    password = models.CharField(max_length=200)
    access_type = models.CharField(max_length=20)
    groups = models.ManyToManyField(to='auth.Group', related_name='author_groups')
    user_permissions = models.ManyToManyField(to='auth.Permission', related_name='author_user_permissions')
    def __str__(self):
        return self.get_full_name()
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        db_table = "author"

# tags information table
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return str(self.tag)

# images information table
class Image(models.Model):
    url = models.URLField(max_length=500)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.url)
    
# blog information table
class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True)
    content = models.TextField(max_length=2500)
    images = models.ManyToManyField(Image)
    estimated_time_to_read = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True,unique=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        return str(self.title)


