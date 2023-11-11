from django.db import models
from datetime import datetime
# author information table
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.BigIntegerField()
    access_type = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.get_full_name()
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

# tags information table
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return str(self.tag)

# blog information table
class Image(models.Model):
    url = models.URLField(max_length=500)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.url)
class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True)
    content = models.TextField(max_length=2500)
    images = models.ManyToManyField(Image)
    estimated_time_to_read = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        return str(self.title)


