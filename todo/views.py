from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView, Response
from django.http import HttpResponseRedirect
from .serializers import getTaskSerializer, postTaskSerializer


class ListView(APIView):
    def get(self, request, *args, **kwargs):  # get request to get all the tasks as index list
        tasks = Task.objects.all()
        serializer = getTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):  # post request to create a new task
        serializer = postTaskSerializer(data=request.data)  # e.g. {"body":"Study DSA"}
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response({"Status": "Posted"})


class TaskView(APIView):
    def get(self, request, taskID, *args, **kwargs):  # get request to get to a specific task
        task = Task.objects.get(pk=taskID)
        serializer = getTaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, taskID, *args, **kwargs):  # delete request to delete a task
        task = Task.objects.get(pk=taskID)
        task.delete()
        return Response({"status": "deleted"})

    def put(self, request, taskID, *args, **kwargs):  # put request to update "completed" status
        task = Task.objects.get(pk=taskID)
        if task.completed == True:
            task.completed = False
        else:
            task.completed = True
        task.save()  # As there are only two possibilities, simply press the "put"
        # button to change status
        return Response({"status": "updated"})

    def patch(self, request, taskID, *args, **kwargs):  # To modify the task(body)
        task = Task.objects.get(pk=taskID)
        serializer = postTaskSerializer(task, data=request.data, partial=True)  # e.g. {"body":"Modified Body"}
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Modified"})
