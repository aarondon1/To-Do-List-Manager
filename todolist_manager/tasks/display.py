from typing import List
from .interfaces import ITask, ITaskDisplay

# Concrete implementations of ITaskDisplay interface
class ConsoleTaskDisplay(ITaskDisplay):
    """Display tasks in console format"""
    
    def display_task(self, task: ITask) -> str:
        details = task.get_details()
        status = "Completed" if details['completed'] else "Pending"
        return f"[{status}] {details['title']} (Priority: {details['priority']})"
    
    def display_task_list(self, tasks: List[ITask]) -> str:
        return "\n".join([self.display_task(task) for task in tasks])

class HtmlTaskDisplay(ITaskDisplay):
    """Display tasks in HTML format"""
    
    def display_task(self, task: ITask) -> str:
        details = task.get_details()
        status_class = "completed" if details['completed'] else "pending"
        return f"""
        <div class="task {status_class}">
            <h3>{details['title']}</h3>
            <p>{details['description']}</p>
            <span class="priority">Priority: {details['priority']}</span>
        </div>
        """
    
    def display_task_list(self, tasks: List[ITask]) -> str:
        return "".join([self.display_task(task) for task in tasks])