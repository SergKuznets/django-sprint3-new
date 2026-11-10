from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published'
    )
    search_fields = (
        'title',
        'description'
    )
    list_filter = (
        'title',
        'description',
        'is_published'
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category'
    )
    search_fields = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category'
    )
    list_filter = (
        'location',
        'category'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
