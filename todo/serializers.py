from .models import Task
from rest_framework import serializers


class getTaskSerializer(serializers.ModelSerializer):  # Index list o all the task
    class Meta:
        model = Task
        fields = ['id', 'body', 'completed']


class postTaskSerializer(serializers.ModelSerializer):  # A specific task view for deletion and changing the status
    class Meta:
        model = Task
        fields = ['body']

# class completedStatusSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Task
#         fields = ['completed']
