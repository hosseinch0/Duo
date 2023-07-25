from django.contrib import admin
from blog.models import Posts
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')
    empty_value_display = "EMPTY"
    list_filter = ('status', 'author')
    search_fields = ('titles',)

admin.site.register(Posts,PostsAdmin)

