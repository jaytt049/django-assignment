from django.contrib import admin
from .models import Blog, Category, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    search_fields = ('title', 'description')
    list_filter = ('category', 'date')
    filter_horizontal = ('tags',)

admin.site.register(Blog, BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)