from django.contrib import admin

from kavete.models import BlogPost, Tag

# Register your models here.
admin.site.site_header = "Kavete's Blog"
admin.site.index_title = "Management"


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Tag, TagAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category']
    search_fields = ['title', 'author', 'category', 'tags']
    list_filter = ['author', 'tags', 'category']


admin.site.register(BlogPost, BlogPostAdmin)
