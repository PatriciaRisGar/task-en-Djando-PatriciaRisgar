from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskView.as_view(), name='tasks_list'),
]