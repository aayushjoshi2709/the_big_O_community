from mongoengine import Document, fields
# author information table
class author(Document):
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    email = fields.EmailField()
    phone_no = fields.BigIntegerField()
    access_type = fields.CharField(max_length=20)
    username = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)

# tags information table
class tags(Document):
    tag = fields.TextField(max_length=50)
# blog information table
class Blog(Document):
    slug = fields.SlugField()
    title = fields.TextField(max_length=300)
    content = fields.CharField(max_length=2500)
    images = [fields.CharField(max_length=100)]
    estimated_time_to_read = fields.IntegerField()
    tags = fields.ManyToManyField(tags)
    author = fields.ForeignKey(author, on_delete=fields.CASCADE)

