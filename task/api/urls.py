from django.urls import path
from task.api.views import (  
task_list,
api_task_detail,
api_task_update,
api_task_delete
)



urlpatterns = [
path('tasks/',task_list, name='task_list' ),
path('task/<int:id>',api_task_detail, name='task_detail'),
path('task/<int:pk>/update',api_task_update, name='task_update'),
path('task/<int:id>/delete',api_task_delete, name='task_delete'),


]
