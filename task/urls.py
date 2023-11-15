from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskView.as_view(), name='tasks_list'),
    path('task/<int:pk>/', views.Task_detail.as_view(), name='task_detail'),
    path('task/task_new', views.Task_new.as_view(), name='task_new'),
]


"""
urlpatterns = [
    path('', views.TaskView, name='tasks_list'),
]
"""