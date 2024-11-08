from rest_framework import serializers
from  task.models import TodoTask
from django.db.models import fields


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoTask
        fields=('title','created','category')
    