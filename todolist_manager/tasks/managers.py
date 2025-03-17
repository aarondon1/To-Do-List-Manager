from typing import List, Optional
from .interfaces import ITaskManager, ITask # import the interfaces to implement the methods
from .models import Task

# funcionality of the task manager, using basic CRUD operations 
class DjangoTaskManager(ITaskManager):
    """Concrete implementation of ITaskManager using Django models"""
    
    def add_task(self, title: str, description: str, priority: int) -> ITask:
        task = Task.objects.create(
            title=title,
            description=description,
            priority=priority
        )
        return task
    
    def mark_completed(self, task_id: int) -> None:
        try:
            task = Task.objects.get(id=task_id)
            task.mark_completed()
        except Task.DoesNotExist:
            pass
    
    def list_tasks(self, status: Optional[bool] = None) -> List[ITask]:
        if status is None:
            return list(Task.objects.all())
        return list(Task.objects.filter(completed=status))
    
    def remove_task(self, task_id: int) -> None:
        try:
            Task.objects.get(id=task_id).delete()
        except Task.DoesNotExist:
            pass