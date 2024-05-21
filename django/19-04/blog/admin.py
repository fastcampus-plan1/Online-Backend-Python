from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]
    list_display_links = ["title"]
    list_filter = ["created_at"]
    search_fields = ["title", "content"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    list_display_links = ["name"]
    list_filter = ["created_at"]
    search_fields = ["name", "message"]
