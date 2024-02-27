from django.contrib import admin

from news.models import New, Comment, Category, Tag


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title',)