from rest_framework import serializers
from .models import Ticket
from accounts.models import User


class TicketSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.username', read_only=True)
    agent_name = serializers.CharField(source='assigned_agent.username', read_only=True, default=None)

    class Meta:
        model = Ticket
        fields = (
            'id', 'title', 'description', 'customer', 'customer_name',
            'assigned_agent', 'agent_name', 'status', 'priority', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'customer', 'created_at', 'updated_at')


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'priority')


class TicketAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('assigned_agent',)

    def validate_assigned_agent(self, value):
        if value.role != 'agent':
            raise serializers.ValidationError("Assigned user must have the 'agent' role.")
        return value


class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('status',)


class TicketPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('priority',)