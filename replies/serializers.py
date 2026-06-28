from rest_framework import serializers
from .models import TicketReply


class TicketReplySerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    sender_role = serializers.CharField(source='sender.role', read_only=True)

    class Meta:
        model = TicketReply
        fields = ('id', 'ticket', 'sender', 'sender_name', 'sender_role', 'message', 'timestamp')
        read_only_fields = ('id', 'sender', 'timestamp')


class TicketReplyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketReply
        fields = ('message',)