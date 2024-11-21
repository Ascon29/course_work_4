from django.contrib import admin

from newsletter.models import Recipient, Message, NewsLetter, Attempt


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment',)
    search_fields = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'head', 'body')
    list_filter = ('head',)
    search_fields = ('head',)


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'status', 'date_of_first_shipment', 'date_of_end_shipment')
    list_filter = ('status', 'message')
    search_fields = ('status', 'message')


@admin.register(Attempt)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_attempt', 'status', 'mail_server_response', 'newsletter')
    list_filter = ('status', 'newsletter')
    search_fields = ('status', 'newsletter')
