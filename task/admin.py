from django.contrib import admin
from task.models import TodoTask,Category


admin.site.register(Category)
admin.site.register(TodoTask)

