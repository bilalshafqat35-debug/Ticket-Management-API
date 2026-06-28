from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'customer', 'assigned_agent', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'customer__username', 'customer__email')
