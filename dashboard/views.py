from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tickets.models import Ticket
from accounts.models import User
from tickets.permissions import IsAgentOrAdmin


class DashboardStatsView(APIView):
    permission_classes = (IsAgentOrAdmin,)

    def get(self, request):
        total_tickets = Ticket.objects.count()
        open_tickets = Ticket.objects.filter(status='open').count()
        in_progress_tickets = Ticket.objects.filter(status='in_progress').count()
        resolved_tickets = Ticket.objects.filter(status='resolved').count()
        closed_tickets = Ticket.objects.filter(status='closed').count()
        active_agents = User.objects.filter(role='agent', is_active=True).count()

        data = {
            'total_tickets': total_tickets,
            'open_tickets': open_tickets,
            'in_progress_tickets': in_progress_tickets,
            'resolved_tickets': resolved_tickets,
            'closed_tickets': closed_tickets,
            'active_agents': active_agents,
        }
        return Response(data)
