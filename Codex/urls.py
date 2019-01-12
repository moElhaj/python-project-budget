from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('project/<int:id>/', views.project, name='project'),
    path('project/new', views.newProject, name='newProject'),
    path('project/delete/<int:id>', views.deleteProject, name='deleteProject'),
    path('task/new', views.newTask, name='newTask'),
    path('task/finish/<int:id>/<int:project>', views.finishTask, name='finishTask'),
    path('task/delete/<int:id>/<int:project>', views.deleteTask, name='deleteTask'),
]
