from django.db import models

# implementing ITask interface
class Task(models.Model):
    """Task model implementing ITask interface"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def mark_completed(self) -> None:
        self.completed = True
        self.save()
    
    def get_details(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_date': self.created_date
        }