from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Ticket
from .serializers import (
    TicketSerializer, TicketCreateSerializer,
    TicketAssignSerializer, TicketStatusSerializer
)
from .permissions import IsAgentOrAdmin


class TicketListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'assigned_agent']
    search_fields = ['title', 'customer__username']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TicketCreateSerializer
        return TicketSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'customer':
            return Ticket.objects.filter(customer=user)
        elif user.role == 'agent':
            return Ticket.objects.filter(assigned_agent=user)
        return Ticket.objects.all()  # admin sees everything

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'customer':
            return Ticket.objects.filter(customer=user)
        elif user.role == 'agent':
            return Ticket.objects.filter(assigned_agent=user)
        return Ticket.objects.all()


class TicketAssignView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketAssignSerializer
    permission_classes = (IsAgentOrAdmin,)


class TicketStatusView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketStatusSerializer
    permission_classes = (IsAgentOrAdmin,)