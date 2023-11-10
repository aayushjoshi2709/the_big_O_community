from django.db import models
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
        return f"{self.first_name} {self.last_name}"

# tags information table
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return str(self.tag)

# blog information table
class Image(models.Model):
    url = models.URLField(max_length=500)
    def __str__(self):
        return str(self.url)
class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=2500)
    images = models.ForeignKey(Image, on_delete=models.CASCADE,null=True)
    estimated_time_to_read = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField()
    def __str__(self):
        return str(self.title)


