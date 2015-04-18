from django.contrib import admin
# from django.contrib import messages
from .models import Front
# from .models import Message


# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'message', 'date')
#     readonly_fields = ('name', 'email', 'phone', 'message', 'date')


class FrontAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Front, FrontAdmin)
# admin.site.register(Message, MessageAdmin)