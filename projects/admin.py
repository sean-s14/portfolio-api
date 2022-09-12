from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _
from .models import Project


class ProjectAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'link', 'imageURI', 'description', 'date_created')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password1', 'password2'),
    #     }),
    # )
    # list_filter = ('is_verified')
    list_display = ('title', 'date_created')


admin.site.register(Project, ProjectAdmin)