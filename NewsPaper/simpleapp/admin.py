from django.contrib import admin
from .models import Category, Post


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(rating=0)
nullfy_quantity.short_description = 'Обнулить рейтинги'


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_in', 'type', 'category', 'rating']
    list_filter = ['type', 'category']
    actions = [nullfy_quantity]

# Register your models here.

admin.site.register(Category)
admin.site.register(Post, PostAdmin)