from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import TicketReply
from .serializers import TicketReplySerializer, TicketReplyCreateSerializer
from tickets.models import Ticket


class TicketReplyListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TicketReplyCreateSerializer
        return TicketReplySerializer

    def get_ticket(self):
        ticket_id = self.kwargs['ticket_id']
        ticket = Ticket.objects.get(id=ticket_id)
        user = self.request.user

        # Role-based access check — sirf related log hi reply/dekh sakte hain
        if user.role == 'customer' and ticket.customer != user:
            raise PermissionDenied("You can only access replies for your own tickets.")
        if user.role == 'agent' and ticket.assigned_agent != user:
            raise PermissionDenied("You can only access replies for tickets assigned to you.")
        # admin ko full access hai, koi restriction nahi

        return ticket

    def get_queryset(self):
        ticket = self.get_ticket()
        return TicketReply.objects.filter(ticket=ticket)

    def perform_create(self, serializer):
        ticket = self.get_ticket()
        serializer.save(ticket=ticket, sender=self.request.user)