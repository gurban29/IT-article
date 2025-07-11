from django.contrib import admin

from .models import *

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'video', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)