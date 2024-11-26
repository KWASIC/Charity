from django.contrib import admin
from .models import Project, Impact

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'goal_amount', 'current_amount', 'start_date', 'end_date')
    list_filter = ('category', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Impact)
class ImpactAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'number', 'created_at')
    list_filter = ('project', 'created_at')
    search_fields = ('title', 'description')
