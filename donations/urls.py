from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('process/<int:project_id>/', views.process_donation, name='process_donation'),
    path('success/', views.donation_success, name='donation_success'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
]
