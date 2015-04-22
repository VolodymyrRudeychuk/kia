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
    list_display = ('name', 'email', 'message', 'date')
    readonly_fields = ('name', 'email', 'message', 'date')


class FrontAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'active')
    list_editable = ('active', )


class StatAdmin(admin.ModelAdmin):
    list_display = ('token_user', 'access_date')
    list_filter = ('access_date', 'token__user')

    def token_user(self, obj):
        return obj.token.user


class CategoryAdmin(admin.ModelAdmin):
    inlines = [MediaInline, ]


admin.site.register(Media, admin.ModelAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Front, FrontAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Statistic, StatAdmin)
admin.site.register(Message, MessageAdmin)