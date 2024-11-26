from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Donation, Subscriber
from projects.models import Project
from .forms import DonationForm, SubscriberForm

# Create your views here.

def donate(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'donations/donate.html', context)

def process_donation(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.project = project
            donation.payment_status = 'completed'  # In real app, this would be handled by payment gateway
            donation.save()
            
            messages.success(request, 'Thank you for your donation!')
            return redirect('donation_success')
    else:
        form = DonationForm()
    
    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'donations/process_donation.html', context)

def donation_success(request):
    return render(request, 'donations/success.html')

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
