from django.db import models
from django.conf import settings
from projects.models import Project

# Create your models here.

class Donation(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField()
    message = models.TextField(blank=True)
    anonymous = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.donor_name} - {self.amount} - {self.project.title}"
    
    def save(self, *args, **kwargs):
        if self.payment_status == 'completed' and not self.pk:
            self.project.current_amount += self.amount
            self.project.save()
        super().save(*args, **kwargs)

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
