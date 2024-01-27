from django.contrib import admin
from .models import Tag, Blog, Author, Image, Social, TeamMembers, Stats
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_filter = ("title","author","date_modified","tags")
    list_display = ("title","author","date_modified")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Tag)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(Social)
admin.site.register(TeamMembers)
admin.site.register(Stats)