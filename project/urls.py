from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/new/', views.projectCreateView, name='new_project'),
    path('project/show/id/<int:id>', views.projectShowView, name='show_project'),
    path('project/delete/id/<int:id>', views.deleteProject, name='delete_project'),
    path('project/delete/all/', views.deleteAllProjects, name='delete_all'),
    ]
