from django.urls import path
from .views import TicketReplyListCreateView

urlpatterns = [
    path('<int:ticket_id>/', TicketReplyListCreateView.as_view(), name='ticket-replies'),
]