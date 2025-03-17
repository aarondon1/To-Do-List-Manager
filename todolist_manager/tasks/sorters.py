from typing import List
from abc import ABC, abstractmethod # because pyhton doesn't have interfaces, we use ABC to create abstract classes (Abstract base classes)
from .interfaces import ITask

# concrete implementations of ITaskSorter interface and how the tasks will be sorted
class ITaskSorter(ABC):
    """Interface for task sorters"""
    @abstractmethod
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        pass

class PrioritySorter(ITaskSorter):
    """Sort tasks by priority"""
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        return sorted(tasks, key=lambda task: task.get_details()['priority'], reverse=True)

class DateSorter(ITaskSorter):
    """Sort tasks by creation date"""
    def sort(self, tasks: List[ITask]) -> List[ITask]:
        return sorted(tasks, key=lambda task: task.get_details()['created_date'])