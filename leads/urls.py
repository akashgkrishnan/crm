from django.urls import path
from .views import (LeadUpdateView, lead_list, lead_detail, lead_create,
                    lead_update, lead_delete,
                    LeadListView, LeadDetailView, LeadCreateView)

app_name = "leads"

urlpatterns = [
    # path('', lead_list, name='lead-list'),
    path('', LeadListView.as_view(), name='lead-list'),
    path('create', LeadCreateView.as_view(), name='lead-create'),
    # path('create/', lead_create, name='lead-create'),
    # path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    # path('update/<int:pk>/', lead_update, name='lead-update'),
    path('delete/<int:pk>/', lead_delete, name='lead-delete'),
]
