from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional information', {'fields': ('date_of_birth', 'bio', 'photo', 'job', 'phone')}),
    )


def make_deactivation(modeladmin, request, queryset):
    result = queryset.update(active=False)
    modeladmin.message_user(request, f'{result} posts were rejected')


make_deactivation.short_description = 'رد پست'


def make_activation(modeladmin, request, queryset):
    result = queryset.update(active=True)
    modeladmin.message_user(request, f'{result} posts were rejected')


make_activation.short_description = 'تایید پست'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'created', 'description']
    ordering = ['created']
    search_fields = ['description']
    inlines = [ImageInline]
    actions = [make_deactivation, make_activation]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'created', 'active']
    list_filter = ['active']
    search_fields = ['name', 'body']
    list_editable = ['active']
    # autocomplete_fields = ['post']


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['post', 'title', 'created']

admin.site.register(Image)
