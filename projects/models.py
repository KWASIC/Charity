from django.db import models
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('healthcare', 'Healthcare'),
        ('food', 'Food'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_progress_percentage(self):
        return int((self.current_amount / self.goal_amount) * 100)
    
    def __str__(self):
        return self.title

class Impact(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='impacts')
    title = models.CharField(max_length=200)
    description = models.TextField()
    number = models.IntegerField(help_text="Numerical impact (e.g., number of students helped)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.project.title}"
