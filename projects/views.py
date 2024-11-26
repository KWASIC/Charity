from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from .models import Project, Impact

# Create your views here.

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:6]
    total_donations = Project.objects.aggregate(total=Sum('current_amount'))['total'] or 0
    total_projects = Project.objects.count()
    total_impacts = Impact.objects.count()
    
    context = {
        'projects': projects,
        'total_donations': total_donations,
        'total_projects': total_projects,
        'total_impacts': total_impacts,
    }
    return render(request, 'projects/home.html', context)

def project_list(request):
    category = request.GET.get('category')
    if category:
        projects = Project.objects.filter(category=category).order_by('-created_at')
    else:
        projects = Project.objects.all().order_by('-created_at')
    
    context = {
        'projects': projects,
        'current_category': category,
    }
    return render(request, 'projects/project_list.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    recent_donations = project.donations.filter(payment_status='completed').order_by('-created_at')[:5]
    impacts = project.impacts.all()
    
    context = {
        'project': project,
        'recent_donations': recent_donations,
        'impacts': impacts,
    }
    return render(request, 'projects/project_detail.html', context)
