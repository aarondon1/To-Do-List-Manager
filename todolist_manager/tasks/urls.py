from django.urls import path
from . import views

# this basically tells Django that when a user goes to the root URL of our site, it should display the task_list view
# and name it 'task_list'
# the name is used in the templates to refer to this URL
# the name is also used in the redirect() function in views.py
# so instead of writing redirect('/'), we can write redirect('task_list')
# this makes the code more maintainable because we only need to change the URL in one place
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]