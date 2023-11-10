from django.contrib import admin
from .models import Tag, Blog, Author,Image
# Register your models here.


admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Image)