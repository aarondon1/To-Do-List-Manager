from typing import List, Optional
from .interfaces import ITaskManager, ITaskDisplay, ITask 
from .sorters import ITaskSorter # import the interfaces to implement the methods

# The Dependency Inversion Principle (DIP) is a software design principle that
# promotes loose coupling and flexibility by advocating that high-level modules should not depend on low-level modules, 
# but both should depend on abstractions.

# The TaskService class is a high-level module that depends on abstractions (interfaces) instead of concrete implementations.
# This would allow the TaskService to be flexible and work with different implemetations of the ITaskManager, ITaskDisplay, and ITaskSorter interfaces.
class TaskService:
    """Service layer for tasks implementing Dependency Inversion"""
    
    def __init__(self, task_manager: ITaskManager, task_display: ITaskDisplay, task_sorter: Optional[ITaskSorter] = None):
        self.task_manager = task_manager
        self.task_display = task_display
        self.task_sorter = task_sorter
    
    def create_task(self, title: str, description: str, priority: int) -> ITask:
        return self.task_manager.add_task(title, description, priority)
    
    def complete_task(self, task_id: int) -> None:
        self.task_manager.mark_completed(task_id)
    
    def delete_task(self, task_id: int) -> None:
        self.task_manager.remove_task(task_id)
    
    def get_tasks(self, status: Optional[bool] = None, sort: bool = False) -> List[ITask]:
        tasks = self.task_manager.list_tasks(status)
        if sort and self.task_sorter:
            tasks = self.task_sorter.sort(tasks)
        return tasks
    
    def get_task_display(self, tasks: List[ITask]) -> str:
        return self.task_display.display_task_list(tasks)