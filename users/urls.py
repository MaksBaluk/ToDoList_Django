from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:user_slug>/', CustomUserDetail.as_view(), name='user_detail'),
    path('<slug:user_slug>/<slug:task_slug>/', ToDoListTaskDetail.as_view(), name='task_detail'),
    path('<slug:user_slug>/addtask', CreateTask.as_view(), name='add_task'),
    path('<slug:user_slug>/updatetask/<slug:task_slug>', UpdateTask.as_view(), name='update_task'),
    path('<slug:user_slug>/deletetask/<slug:task_slug>', DeleteTask.as_view(), name='delete_task'),
    path('<slug:user_slug>/<slug:task_slug>/update-is-complete/', UpdateIsCompleteView.as_view(),
         name='update_is_complete'),
    path('<slug:user_slug>/<slug:task_slug>/update-is-private/', UpdateIsPrivateView.as_view(),
         name='update_is_private'),
]
