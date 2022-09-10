from django.contrib import admin
from django.contrib.admin import ModelAdmin
from markdownx.admin import MarkdownxModelAdmin
from django.utils.translation import gettext_lazy as _
from .models import Article


class ArticleAdmin(MarkdownxModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'date_created', 'text', 'imageURI')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password1', 'password2'),
    #     }),
    # )
    # list_filter = ('is_verified')
    list_display = ('title', 'id', 'date_created')


admin.site.register(Article, ArticleAdmin)