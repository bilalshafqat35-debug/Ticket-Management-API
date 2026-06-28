from django.contrib import admin
from .models import TicketReply


@admin.register(TicketReply)
class TicketReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'sender', 'timestamp')
    search_fields = ('message',)
