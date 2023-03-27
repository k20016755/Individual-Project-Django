from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    due = models.DateTimeField()

    def __str__(self):
        return self.title

# Create your models here.
