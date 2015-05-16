from django.contrib import admin
# from django.contrib import messages
from .models import (
    Front,
    Token,
    Statistic,
    Message,
    Category,
    Media
)
# from .models import Message

class MediaInline(admin.TabularInline):
    model = Media

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sc_name', 'email', 'date')
    readonly_fields = ('sc_name', 'email', 'date')

    def sc_name(self, obj):
        return obj.school.first_name or obj.school


class FrontAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'active')
    list_editable = ('active', )


class StatAdmin(admin.ModelAdmin):
    list_display = ('user', 'access_date')
    list_filter = ('access_date', 'user')


class CategoryAdmin(admin.ModelAdmin):
    inlines = [MediaInline, ]
    list_filter = ('type', 'language', 'grade')





admin.site.register(Media, admin.ModelAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Front, FrontAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Statistic, StatAdmin)
admin.site.register(Message, MessageAdmin)
