from django.urls import path
from .views import (
    TicketListCreateView, TicketDetailView,
    TicketAssignView, TicketStatusView, TicketPriorityView
)

urlpatterns = [
    path('', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('<int:pk>/assign/', TicketAssignView.as_view(), name='ticket-assign'),
    path('<int:pk>/status/', TicketStatusView.as_view(), name='ticket-status'),
    path('<int:pk>/priority/', TicketPriorityView.as_view(), name='ticket-priority'),
]