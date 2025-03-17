# To-Do List Manager

A Django-based To-Do List Manager that follows SOLID principles and object-oriented design.

## Basic Features

- Add tasks with title, description, and priority
- Mark tasks as completed
- List all tasks with filtering options
- Delete tasks
- Sort tasks by priority

## Architecture

This project demonstrates SOLID principles:

- **Single Responsibility Principle**: Each class has one responsibility
- **Open-Closed Principle**: New functionality can be added through extension
- **Liskov Substitution Principle**: Implementations are interchangeable
- **Interface Segregation Principle**: Interfaces are focused and minimal
- **Dependency Inversion Principle**: High-level modules depend on abstractions

## How to run this...

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment: `.venv\Scripts\activate`, for MACOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. If you make any changes remeber to `python manage.py makemigrations` then to...
6. Run migrations: `python manage.py migrate`
7. Start the server: `python manage.py runserver`

## Project Structure

- `interfaces.py`: Contains all interface definitions
- `models.py`: Django models implementing interfaces
- `managers.py`: Task management implementation
- `display.py`: Different ways to display tasks
- `sorters.py`: Task sorting strategies
- `services.py`: Service layer coordinating components
- `views.py`: Django views using the service layer
