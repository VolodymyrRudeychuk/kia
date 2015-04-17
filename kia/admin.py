from django.contrib import admin
from .models import Front


class FrontAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Front, FrontAdmin)