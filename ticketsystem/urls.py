from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_welcome(request):
    return JsonResponse({
        "message": "Customer Support Ticket Management API is live",
        "endpoints": {
            "register": "/api/auth/register/",
            "login": "/api/auth/login/",
            "profile": "/api/auth/profile/",
            "tickets": "/api/tickets/",
            "dashboard_stats": "/api/dashboard/stats/",
            "admin_panel": "/admin/"
        }
    })


urlpatterns = [
    path('', api_welcome),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/tickets/', include('tickets.urls')),
    path('api/tickets/replies/', include('replies.urls')),
    path('api/dashboard/', include('dashboard.urls')),
]