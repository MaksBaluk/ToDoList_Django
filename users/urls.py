from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:user_slug>/', CustomUserDetail.as_view(), name='user_detail'),
    path('<slug:user_slug>/<slug:task_slug>/', ToDoListTaskDetail.as_view(), name='task_detail'),
    path('<slug:user_slug>/addtask', CreateTask.as_view(), name='add_task'),
]
