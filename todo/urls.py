from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='List_Screen'),
    path('<int:taskID>/', views.TaskView.as_view(), name='Detailed_Task'),
    # path('<int:taskID>/completed', views.TaskStatus.as_view(), name='Update'),
]