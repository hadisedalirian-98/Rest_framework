from django.urls import path
from task.views import (
    showtask
    ,TaskDetail
    ,delete_task)

urlpatterns = [
path('',showtask,name='showtask' ),
path('task/<int:pk>',TaskDetail.as_view(), name='task_detail' ),
path('<int:id>',delete_task,name='delete_task' ),

]
