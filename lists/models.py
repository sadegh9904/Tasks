from django.db import models
from jalali_date import date2jalali

# Create your models here.

class TaskView(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True,null=True,editable=True)

    def __str__(self):
        return f"{self.name} {self.description}"
    
    def get_jalali(self):
        return date2jalali(self.created_at)
        