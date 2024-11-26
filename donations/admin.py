from django.contrib import admin
from .models import Donation, Subscriber

# Register your models here.

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'amount', 'project', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'created_at', 'project')
    search_fields = ('donor_name', 'donor_email', 'message')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subscribed_at')
    search_fields = ('email', 'name')
