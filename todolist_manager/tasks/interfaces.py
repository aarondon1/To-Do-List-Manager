from abc import ABC, abstractmethod # because pyhton doesn't have interfaces, we use ABC to create abstract classes (Abstract base classes)
from typing import List, Optional # for type hinting

# Interfaces for Task, TaskManager and TaskDisplay
class ITask(ABC):
    """Interface for Task objects"""
    @abstractmethod
    def mark_completed(self) -> None:
        pass
    
    @abstractmethod
    def get_details(self) -> dict:
        pass

class ITaskManager(ABC):
    """Interface for Task Manager"""
    @abstractmethod
    def add_task(self, title: str, description: str, priority: int) -> ITask:
        pass
    
    @abstractmethod
    def mark_completed(self, task_id: int) -> None:
        pass
    
    @abstractmethod
    def list_tasks(self, status: Optional[bool] = None) -> List[ITask]:
        pass
    
    @abstractmethod
    def remove_task(self, task_id: int) -> None:
        pass

class ITaskDisplay(ABC):
    """Interface for displaying tasks"""
    @abstractmethod
    def display_task(self, task: ITask) -> str:
        pass
    
    @abstractmethod
    def display_task_list(self, tasks: List[ITask]) -> str:
        pass