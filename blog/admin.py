from django.contrib import admin
from models import Post, Comments


class PostInline(admin.StackedInline):
    model = Comments


class PostAdmin(admin.ModelAdmin):
    inlines = [PostInline]

admin.site.register(Post, PostAdmin)


